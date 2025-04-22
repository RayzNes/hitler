import pygame
import asyncio
import platform
import random
import logging
from player import Player
from missions import get_mission, adjust_success_chance
from events import get_event
from ui import draw_text, render_game_state, initialize_fonts
from savegame import save_game, load_game
from game_config import WIDTH, HEIGHT, FPS, DIFFICULTY_MODIFIERS, DEBUG_MODE

# Настройка логирования
logging.basicConfig(filename="game.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Инициализация Pygame
pygame.init()
initialize_fonts()

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Кризис Командования")

# Глобальные переменные
player = Player()
game_state = "start"
current_mission = None
current_event = None
choices = []
result_text = []
running = True
sandbox_mode = False
difficulty = "normal"
event_chance = DIFFICULTY_MODIFIERS["normal"]["event_chance"]

def setup(difficulty_level="normal"):
    global player, game_state, current_mission, current_event, choices, result_text, sandbox_mode, difficulty, event_chance
    player = Player()
    difficulty = difficulty_level
    resource_bonus = DIFFICULTY_MODIFIERS[difficulty]["resource_bonus"]
    event_chance = DIFFICULTY_MODIFIERS[difficulty]["event_chance"]
    player.army += resource_bonus
    player.fuel += resource_bonus
    player.support += resource_bonus
    player.economy += resource_bonus
    player.tech += resource_bonus
    player.morale += resource_bonus
    player.reputation += resource_bonus
    game_state = "start"
    current_mission = None
    current_event = None
    choices = []
    result_text = []
    sandbox_mode = False
    logging.info(f"Game reset. Difficulty: {difficulty}. Resource bonus: {resource_bonus}, Event chance: {event_chance}")

def check_region_penalties():
    """Проверяет потерю регионов и применяет штрафы."""
    for region, control in player.regions.items():
        if control <= 0:
            player.economy -= 20
            player.support -= 20
            player.morale -= 10
            player.regions[region] = 0
            result_text.append(f"Регион {region} потерян! Экономика -20, Поддержка -20, Мораль -10.")
            logging.info(f"Region {region} lost. Economy -20, Support -20, Morale -10.")

def check_relations_bonuses_penalties():
    """Проверяет бонусы и штрафы от отношений."""
    for ally, value in player.relations.items():
        if value > 70:
            if ally == "Japan":
                player.fuel += 10
                result_text.append(f"Япония поставляет топливо: +10 топлива.")
                logging.info("Japan bonus: +10 fuel.")
            elif ally == "Italy":
                player.army += 5
                result_text.append(f"Италия усиливает армию: +5 армии.")
                logging.info("Italy bonus: +5 army.")
        elif value < 10:
            player.support -= 15
            player.relations[ally] = 0
            result_text.append(f"{ally} разрывает альянс! Поддержка -15.")
            logging.info(f"{ally} alliance broken. Support -15.")

def check_investments():
    """Проверяет и применяет эффекты долгосрочных инвестиций."""
    for investment in player.investments[:]:
        investment["turns_left"] -= 1
        if investment["turns_left"] <= 0:
            for resource, value in investment["effect"].items():
                setattr(player, resource, getattr(player, resource) + value)
            result_text.append(f"Инвестиция '{investment['type']}' завершена! Эффект: {', '.join([f'{k}: +{v}' for k, v in investment['effect'].items()])}")
            logging.info(f"Investment '{investment['type']}' completed. Effects: {investment['effect']}")
            player.investments.remove(investment)

def check_consecutive_successes():
    """Проверяет серию успешных миссий и начисляет бонусы."""
    if player.consecutive_successes >= 3:
        bonuses = [
            {"fuel": 20, "text": "Серия успехов! +20 топлива."},
            {"morale": 10, "text": "Серия успехов! +10 морали."},
            {"support": 15, "text": "Серия успехов! +15 поддержки."}
        ]
        bonus = random.choice(bonuses)
        for resource, value in bonus.items():
            if resource != "text":
                setattr(player, resource, getattr(player, resource) + value)
        result_text.append(bonus["text"])
        logging.info(f"Consecutive success bonus: {bonus['text']}")
        player.consecutive_successes = 0

def check_goals():
    """Проверяет выполнение долгосрочных целей и начисляет бонусы."""
    if player.year >= 1945 and player.regions["east"] > 50 and not player.goals["hold_east_1945"]["completed"]:
        player.goals["hold_east_1945"]["completed"] = True
        player.support += 50
        player.morale += 20
        result_text.append("Цель достигнута: Удержать Восточный фронт до 1945 года! Поддержка +50, Мораль +20.")
        logging.info("Goal achieved: Hold East Front 1945. Support +50, Morale +20.")

    if "Финансировать проект V-2" in player.history and not player.goals["develop_v2"]["completed"]:
        player.goals["develop_v2"]["completed"] = True
        player.tech += 30
        player.support += 20
        result_text.append("Цель достигнута: Разработать V-2! Технологии +30, Поддержка +20.")
        logging.info("Goal achieved: Develop V-2. Tech +30, Support +20.")

    if player.year >= 1944 and player.support > 70 and not player.goals["high_support_1944"]["completed"]:
        player.goals["high_support_1944"]["completed"] = True
        player.economy += 30
        player.morale += 15
        result_text.append("Цель достигнута: Сохранить поддержку выше 70 в 1944 году! Экономика +30, Мораль +15.")
        logging.info("Goal achieved: High support 1944. Economy +30, Morale +15.")

def set_ending():
    """Определяет концовку игры."""
    if player.successful_missions > 10 and player.year >= 1945:
        player.ending_text = "Вы переломили ход войны, но победа недостижима. Ваши усилия вошли в историю."
    elif player.support < 10:
        player.ending_text = "Народ восстал, режим пал. Ваше правление закончилось в хаосе."
    elif player.army < 10:
        player.ending_text = "Ваши армии разбиты, враг в Берлине. Германия капитулировала."
    elif player.reputation < 10:
        player.ending_text = "Ваша репутация разрушена. Мир отвернулся от вас, и союзники покинули."
    else:
        player.ending_text = (
            "Раннее поражение: Германия пала в 1943." if player.year == 1943 else
            "Вы продержались до 1944, но силы иссякли." if player.year == 1944 else
            "Удержание позиций до 1945: редкий успех."
        )
    logging.info(f"Game over. Ending: {player.ending_text}")

def apply_event_effects(choice_idx=None):
    """Применяет эффекты события, учитывая смягчение катастроф."""
    event_effects = current_event["effect"].copy()

    # Смягчение последствий катастроф
    if current_event.get("id") == "berlin_bombing":
        if player.bomb_shelters_built:
            for resource in event_effects:
                event_effects[resource] = int(event_effects[resource] * 0.5)  # Урон снижен на 50%
            result_text.append("Бомбоубежища смягчили урон от бомбардировки!")
            logging.info("Berlin bombing mitigated by bomb shelters.")
        elif player.tech > 70:
            for resource in event_effects:
                event_effects[resource] = int(event_effects[resource] * 0.75)  # Урон снижен на 25%
            result_text.append("Высокие технологии снизили урон от бомбардировки!")
            logging.info("Berlin bombing mitigated by high tech.")

    if current_event.get("id") == "rear_epidemic" and player.economy > 70:
        for resource in event_effects:
            event_effects[resource] = int(event_effects[resource] * 0.75)  # Урон снижен на 25%
        result_text.append("Сильная экономика позволила справиться с эпидемией!")
        logging.info("Rear epidemic mitigated by strong economy.")

    if current_event["choices"] and choice_idx is not None:
        choice = current_event["choices"][choice_idx]
        success = random.random() < choice.get("success_chance", 1.0)
        if success:
            for resource, value in choice["effect"].items():
                if resource == "relations_change":
                    for ally, rel_value in value.items():
                        player.relations[ally] = max(0, min(100, player.relations[ally] + rel_value))
                else:
                    setattr(player, resource, getattr(player, resource) + value)
            result_text.append(f"Успех! {choice['text'].lower()} прошло успешно.")
            logging.info(f"Event choice success: {choice['text']}")
        else:
            player.support -= 10
            result_text.append(f"Провал! {choice['text'].lower()} не удалось. Поддержка -10.")
            logging.info(f"Event choice failed: {choice['text']}. Support -10.")
    else:
        for resource, value in event_effects.items():
            if resource == "relations_change":
                for ally, rel_value in value.items():
                    player.relations[ally] = max(0, min(100, player.relations[ally] + rel_value))
            else:
                setattr(player, resource, getattr(player, resource) + value)

    if current_event["region"] and current_event["region"] in player.regions:
        player.regions[current_event["region"]] += current_event["region_change"]
        player.regions[current_event["region"]] = max(0, min(100, player.regions[current_event["region"]]))

    if current_event.get("id"):
        player.event_history.append(current_event["id"])
    check_region_penalties()
    check_relations_bonuses_penalties()
    logging.info(f"Event applied. Resources: army={player.army}, fuel={player.fuel}, support={player.support}, economy={player.economy}, tech={player.tech}, morale={player.morale}, reputation={player.reputation}")

def process_choice(choice_idx):
    global game_state, result_text
    choice = choices[choice_idx]
    # Применение бонуса Шпеера (снижение затрат экономики)
    economy_cost = choice["economy_cost"]
    if player.leaders["Speer"]["active"]:
        economy_cost = int(economy_cost * (1 - player.leaders["Speer"]["bonus"]["economy_cost_reduction"]))
    player.army -= choice["army_cost"]
    player.fuel -= choice["fuel_cost"]
    player.support -= choice["support_cost"]
    player.economy -= economy_cost
    player.tech -= choice["tech_cost"]
    player.morale += choice["morale_change"]
    player.reputation += choice.get("reputation_change", 0)
    player.morale = max(0, min(100, player.morale))
    player.reputation = max(0, min(100, player.reputation))
    for ally, value in choice["relations_change"].items():
        player.relations[ally] = max(0, min(100, player.relations[ally] + value))
    player.decisions += 1
    success = random.random() < choice["success_chance"]
    player.successful_missions += 1 if success else 0
    player.consecutive_successes = player.consecutive_successes + 1 if success else 0
    player.history.append(choice["text"])
    if choice["text"] == "Усилить пропаганду":
        player.turns_since_propaganda = 0
    else:
        player.turns_since_propaganda += 1
    if choice["text"] == "Построить бомбоубежища":
        player.bomb_shelters_built = True
    if choice.get("investment"):
        player.investments.append(choice["investment"])
        logging.info(f"Investment started: {choice['investment']['type']}, Turns: {choice['investment']['turns_left']}")

    if current_mission["region"] and current_mission["region"] in player.regions:
        player.regions[current_mission["region"]] += choice["region_change"]
        player.regions[current_mission["region"]] = max(0, min(100, player.regions[current_mission["region"]]))

    if player.decisions % 5 == 0:
        player.year += 1

    if success:
        player.support += choice["reward"]
        player.economy += choice["reward"] // 2
        player.tech += choice["reward"] // 4
        player.morale += 5
        player.morale = max(0, min(100, player.morale))
        result_text = [
            f"Успех! {choice['text'].lower()} прошло успешно. Поддержка +{choice['reward']}, "
            f"Экономика +{choice['reward'] // 2}, Технологии +{choice['reward'] // 4}, Мораль +5."]
        logging.info(f"Mission success: {choice['text']}. Support +{choice['reward']}, Economy +{choice['reward'] // 2}, Tech +{choice['reward'] // 4}, Morale +5.")
    else:
        player.support -= 20
        player.economy -= 10
        player.morale -= 10
        player.morale = max(0, min(100, player.morale))
        result_text = [f"Провал! {choice['text'].lower()} не удалось. Поддержка -20, Экономика -10, Мораль -10."]
        logging.info(f"Mission failed: {choice['text']}. Support -20, Economy -10, Morale -10.")

    check_region_penalties()
    check_relations_bonuses_penalties()
    check_investments()
    check_consecutive_successes()
    check_goals()

    if not player.is_alive():
        set_ending()
        result_text.append("Вы потеряли контроль. Игра окончена.")
    else:
        result_text.append("Готовьтесь к следующей миссии.")

    save_game(player, autosave=True)  # Автосохранение после выбора
    game_state = "result"

def update_loop():
    global game_state, current_mission, current_event, choices, result_text, running, sandbox_mode

    if DEBUG_MODE:
        print(f"State: {game_state}, Mission: {current_mission}, Event: {current_event}, Choices: {len(choices)}")

    mouse_pos = pygame.mouse.get_pos() if game_state not in ["start", "game_over", "stats"] else None

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game(player, autosave=True)  # Автосохранение при выходе
            running = False
            pygame.quit()
            logging.info("Game quit.")
            return
        if event.type == pygame.KEYDOWN:
            if game_state == "start":
                if event.key == pygame.K_1:
                    setup("easy")
                    game_state = "mission"
                    current_mission = get_mission(player.history, player)
                    adjust_success_chance(current_mission, player)
                    choices = current_mission["choices"]
                    logging.info(f"Game started. Difficulty: easy")
                elif event.key == pygame.K_2:
                    setup("normal")
                    game_state = "mission"
                    current_mission = get_mission(player.history, player)
                    adjust_success_chance(current_mission, player)
                    choices = current_mission["choices"]
                    logging.info(f"Game started. Difficulty: normal")
                elif event.key == pygame.K_3:
                    setup("hard")
                    game_state = "mission"
                    current_mission = get_mission(player.history, player)
                    adjust_success_chance(current_mission, player)
                    choices = current_mission["choices"]
                    logging.info(f"Game started. Difficulty: hard")
                elif event.key == pygame.K_l:
                    loaded_player = load_game()
                    if loaded_player:
                        player.__dict__.update(loaded_player.__dict__)
                        game_state = "mission"
                        current_mission = get_mission(player.history, player)
                        adjust_success_chance(current_mission, player)
                        choices = current_mission["choices"]
                        result_text = ["Игра успешно загружена!"]
                        logging.info("Game loaded successfully.")
                    else:
                        result_text = ["Ошибка загрузки: сохранение не найдено или повреждено."]
                        logging.error("Game load failed.")
                elif event.key == pygame.K_p and DEBUG_MODE:
                    sandbox_mode = True
                    setup("normal")
                    game_state = "mission"
                    current_mission = get_mission(player.history, player)
                    adjust_success_chance(current_mission, player)
                    choices = current_mission["choices"]
                    player.army = 999
                    player.fuel = 999
                    player.support = 999
                    player.economy = 999
                    player.tech = 999
                    player.morale = 999
                    player.reputation = 999
                    result_text = ["Песочница активирована: ресурсы максимальны!"]
                    logging.info("Sandbox mode activated.")
            elif game_state == "mission":
                if event.key == pygame.K_SPACE:
                    game_state = "choice"
                elif event.key == pygame.K_t:
                    game_state = "stats"
            elif game_state == "choice":
                if event.key == pygame.K_1:
                    process_choice(0)
                elif event.key == pygame.K_2:
                    process_choice(1)
                elif event.key == pygame.K_3:
                    process_choice(2)
                elif event.key == pygame.K_s:
                    if save_game(player):
                        result_text = ["Игра успешно сохранена!"]
                        logging.info("Game saved manually.")
                    else:
                        result_text = ["Ошибка сохранения!"]
                        logging.error("Manual save failed.")
                elif event.key == pygame.K_t:
                    game_state = "stats"
            elif game_state == "event":
                if current_event["choices"]:
                    if event.key == pygame.K_1:
                        apply_event_effects(0)
                        game_state = "result"
                        save_game(player, autosave=True)  # Автосохранение
                    elif event.key == pygame.K_2:
                        apply_event_effects(1)
                        game_state = "result"
                        save_game(player, autosave=True)  # Автосохранение
                elif event.key == pygame.K_SPACE:
                    apply_event_effects()
                    game_state = "mission"
                    current_mission = get_mission(player.history, player)
                    adjust_success_chance(current_mission, player)
                    choices = current_mission["choices"]
                    current_event = None
                    save_game(player, autosave=True)  # Автосохранение
                if event.key == pygame.K_t:
                    game_state = "stats"
            elif game_state == "result":
                if event.key == pygame.K_SPACE:
                    if player.is_alive():
                        if random.random() < event_chance or sandbox_mode:
                            game_state = "event"
                            current_event = get_event(player.history, player)
                            logging.info(f"Event triggered: {current_event['text']}")
                        else:
                            game_state = "mission"
                            current_mission = get_mission(player.history, player)
                            adjust_success_chance(current_mission, player)
                            choices = current_mission["choices"]
                            logging.info(f"Mission triggered: {current_mission['text']}")
                        result_text = []
                    else:
                        game_state = "game_over"
                elif event.key == pygame.K_s:
                    if save_game(player):
                        result_text = ["Игра успешно сохранена!"]
                        logging.info("Game saved manually.")
                    else:
                        result_text = ["Ошибка сохранения!"]
                        logging.error("Manual save failed.")
                elif event.key == pygame.K_t:
                    game_state = "stats"
            elif game_state == "game_over" and event.key == pygame.K_r:
                setup(difficulty)
            elif game_state == "stats" and event.key == pygame.K_t:
                game_state = "mission" if current_mission else "result" if result_text else "event"

    render_game_state(screen, game_state, player, current_mission, current_event, choices, result_text, DEBUG_MODE, mouse_pos)

async def main():
    setup()
    while running:
        update_loop()
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())