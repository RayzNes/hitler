import pygame
import asyncio
import platform
import random
from player import Player
from missions import get_mission
from events import get_event
from ui import draw_text, render_game_state, initialize_fonts
from savegame import save_game, load_game

# Инициализация Pygame
pygame.init()
initialize_fonts()

# Константы
WIDTH = 800
HEIGHT = 600
FPS = 60
EVENT_CHANCE = 0.3  # Вероятность события
DEBUG_MODE = False  # Режим отладки

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


def setup():
    global player, game_state, current_mission, current_event, choices, result_text
    player = Player()
    game_state = "start"
    current_mission = None
    current_event = None
    choices = []
    result_text = []


def update_loop():
    global game_state, current_mission, current_event, choices, result_text, running

    if DEBUG_MODE:
        print(f"State: {game_state}, Mission: {current_mission}, Event: {current_event}, Choices: {len(choices)}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            return
        if event.type == pygame.KEYDOWN:
            if game_state == "start":
                if event.key == pygame.K_SPACE:
                    game_state = "mission"
                    current_mission = get_mission(player.history)
                    choices = current_mission["choices"]
                elif event.key == pygame.K_l:  # Загрузить игру
                    loaded_player = load_game()
                    if loaded_player:
                        player.__dict__.update(loaded_player.__dict__)
                        game_state = "mission"
                        current_mission = get_mission(player.history)
                        choices = current_mission["choices"]
                        result_text = ["Игра успешно загружена!"]
                    else:
                        result_text = ["Ошибка загрузки: сохранение не найдено или повреждено."]
            elif game_state == "mission" and event.key == pygame.K_SPACE:
                game_state = "choice"
            elif game_state == "choice":
                if event.key == pygame.K_1:
                    process_choice(0)
                elif event.key == pygame.K_2:
                    process_choice(1)
                elif event.key == pygame.K_3:
                    process_choice(2)
                elif event.key == pygame.K_s:  # Сохранить игру
                    if save_game(player):
                        result_text = ["Игра успешно сохранена!"]
                    else:
                        result_text = ["Ошибка сохранения!"]
            elif game_state == "result" and event.key == pygame.K_SPACE:
                if player.is_alive():
                    if random.random() < EVENT_CHANCE:
                        game_state = "event"
                        current_event = get_event(player.history)
                    else:
                        game_state = "mission"
                        current_mission = get_mission(player.history)
                        choices = current_mission["choices"]
                    result_text = []
                else:
                    game_state = "game_over"
            elif game_state == "event" and event.key == pygame.K_SPACE:
                game_state = "mission"
                current_mission = get_mission(player.history)
                choices = current_mission["choices"]
                current_event = None
            elif game_state == "game_over" and event.key == pygame.K_r:
                setup()
            elif event.key == pygame.K_s and game_state == "result":  # Сохранить игру
                if save_game(player):
                    result_text = ["Игра успешно сохранена!"]
                else:
                    result_text = ["Ошибка сохранения!"]

    # Отрисовка
    render_game_state(screen, game_state, player, current_mission, current_event, choices, result_text, DEBUG_MODE)


def process_choice(choice_idx):
    global game_state, result_text
    choice = choices[choice_idx]
    player.army -= choice["army_cost"]
    player.fuel -= choice["fuel_cost"]
    player.support -= choice["support_cost"]
    player.economy -= choice["economy_cost"]
    player.decisions += 1
    player.successful_missions += 1 if random.random() < choice["success_chance"] else 0
    player.history.append(choice["text"])  # Сохраняем выбор

    if player.decisions % 5 == 0:
        player.year += 1  # Прогресс года

    if random.random() < choice["success_chance"]:
        player.support += choice["reward"]
        player.economy += choice["reward"] // 2
        result_text = [
            f"Успех! {choice['text'].lower()} прошло успешно. Поддержка +{choice['reward']}, Экономика +{choice['reward'] // 2}."]
    else:
        player.support -= 20
        player.economy -= 10
        result_text = [f"Провал! {choice['text'].lower()} не удалось. Поддержка -20, Экономика -10."]

    if not player.is_alive():
        result_text.append("Вы потеряли контроль. Игра окончена.")
    else:
        result_text.append("Готовьтесь к следующей миссии.")

    game_state = "result"


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