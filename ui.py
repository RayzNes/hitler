import pygame
import math
import random

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Переменные для шрифтов
font = None
small_font = None

# Переменная для анимации
animation_time = 0

# Исторические факты по годам
historical_facts = {
    1943: [
        "1943: Сталинградская битва завершилась победой СССР.",
        "1943: Союзники высадились на Сицилии, начав Итальянскую кампанию.",
        "1943: Курская битва стала крупнейшим танковым сражением в истории."
    ],
    1944: [
        "1944: Операция 'Багратион' освободила Белоруссию от немецкой оккупации.",
        "1944: Высадка в Нормандии открыла Западный фронт.",
        "1944: Варшавское восстание было подавлено немецкими войсками."
    ],
    1945: [
        "1945: Советские войска вошли в Берлин, завершая войну в Европе.",
        "1945: Ялтинская конференция определила послевоенное устройство мира.",
        "1945: Первое применение V-2 против Лондона."
    ]
}

def initialize_fonts():
    global font, small_font
    font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 28)

def draw_text(screen, text, font_obj, color, x, y, wrap_width=None):
    if wrap_width:
        words = text.split(" ")
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font_obj.size(test_line)[0] <= wrap_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        for i, line in enumerate(lines):
            text_surface = font_obj.render(line, True, color)
            screen.blit(text_surface, (x, y + i * font_obj.get_height()))
        return len(lines) * font_obj.get_height()
    else:
        text_surface = font_obj.render(text, True, color)
        screen.blit(text_surface, (x, y))
        return font_obj.get_height()

def draw_map(screen, player):
    """Отрисовка карты с регионами."""
    global animation_time
    animation_time += 0.05  # Скорость анимации
    alpha = 255 * (0.5 + 0.5 * math.sin(animation_time))  # Мигающий эффект

    regions = [
        {"name": "Восточный фронт", "x": 750, "y": 50, "w": 200, "h": 50, "key": "east"},
        {"name": "Западный фронт", "x": 750, "y": 120, "w": 200, "h": 50, "key": "west"},
        {"name": "Африка", "x": 750, "y": 190, "w": 200, "h": 50, "key": "africa"}
    ]

    for region in regions:
        control = player.regions[region["key"]]
        if control > 60:
            color = GREEN
        elif control > 30:
            color = YELLOW
        else:
            color = RED
            color = (*color[:3], int(alpha))

        rect = pygame.Rect(region["x"], region["y"], region["w"], region["h"])
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        draw_text(screen, f"{region['name']}: {control}%", small_font, BLACK, region["x"] + 5, region["y"] + 15)

def render_game_state(screen, game_state, player, current_mission, current_event, choices, result_text, debug_mode):
    screen.fill(GRAY)

    if game_state not in ["start", "game_over"]:
        draw_map(screen, player)

    if game_state == "start":
        draw_text(screen, "Кризис Командования", font, BLACK, 50, 50)
        draw_text(screen, "1943 год. Вы стоите во главе Германии в разгар войны. Ваши решения определят судьбу.",
                  small_font, BLACK, 50, 150, 900)
        draw_text(screen, "Нажмите ПРОБЕЛ для начала или L для загрузки", font, BLACK, 50, 300)
    elif game_state == "mission":
        stats = (f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  "
                 f"Поддержка: {player.support}  Экономика: {player.economy}  "
                 f"Технологии: {player.tech}  Мораль: {player.morale}  Решения: {player.decisions}  "
                 f"Италия: {player.relations['Italy']}  Япония: {player.relations['Japan']}  Нейтралы: {player.relations['Neutral']}")
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy, player.tech, player.morale]) else BLACK,
                  50, 50, 700)
        # Отображение целей
        goals_text = "Цели: " + ", ".join([f"{goal['description']} [{'✓' if goal['completed'] else ' '}]" for goal in player.goals.values()])
        draw_text(screen, goals_text, small_font, BLACK, 50, 100, 700)
        draw_text(screen, "Новая миссия начинается...", small_font, BLACK, 50, 150, 700)
        draw_text(screen, current_mission["text"], small_font, BLACK, 50, 200, 700)
        # Историческая справка
        fact = random.choice(historical_facts.get(player.year, ["Исторических данных нет."]))
        draw_text(screen, f"История: {fact}", small_font, BLACK, 50, 300, 700)
        draw_text(screen, "Нажмите ПРОБЕЛ для продолжения", font, BLACK, 50, 350)
    elif game_state == "choice":
        stats = (f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  "
                 f"Поддержка: {player.support}  Экономика: {player.economy}  "
                 f"Технологии: {player.tech}  Мораль: {player.morale}  Решения: {player.decisions}  "
                 f"Италия: {player.relations['Italy']}  Япония: {player.relations['Japan']}  Нейтралы: {player.relations['Neutral']}")
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy, player.tech, player.morale]) else BLACK,
                  50, 50, 700)
        goals_text = "Цели: " + ", ".join([f"{goal['description']} [{'✓' if goal['completed'] else ' '}]" for goal in player.goals.values()])
        draw_text(screen, goals_text, small_font, BLACK, 50, 100, 700)
        draw_text(screen, current_mission["text"], small_font, BLACK, 50, 150, 700)
        for i, choice in enumerate(choices):
            draw_text(screen, f"{i + 1}. {choice['text']} ({choice['hint']})", small_font, BLACK, 50, 250 + i * 50, 700)
        draw_text(screen, "Нажмите 1, 2 или 3 для выбора, S для сохранения", font, BLACK, 50, 450)
    elif game_state == "event":
        stats = (f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  "
                 f"Поддержка: {player.support}  Экономика: {player.economy}  "
                 f"Технологии: {player.tech}  Мораль: {player.morale}  Решения: {player.decisions}  "
                 f"Италия: {player.relations['Italy']}  Япония: {player.relations['Japan']}  Нейтралы: {player.relations['Neutral']}")
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy, player.tech, player.morale]) else BLACK,
                  50, 50, 700)
        goals_text = "Цели: " + ", ".join([f"{goal['description']} [{'✓' if goal['completed'] else ' '}]" for goal in player.goals.values()])
        draw_text(screen, goals_text, small_font, BLACK, 50, 100, 700)
        draw_text(screen, "Событие!", small_font, BLACK, 50, 150, 700)
        draw_text(screen, current_event["text"], small_font, BLACK, 50, 200, 700)
        # Историческая справка
        fact = random.choice(historical_facts.get(player.year, ["Исторических данных нет."]))
        draw_text(screen, f"История: {fact}", small_font, BLACK, 50, 300, 700)
        if current_event["choices"]:
            for i, choice in enumerate(current_event["choices"]):
                draw_text(screen, f"{i + 1}. {choice['text']}", small_font, BLACK, 50, 250 + i * 50, 700)
            draw_text(screen, "Нажмите 1 или 2 для выбора", font, BLACK, 50, 350)
        else:
            draw_text(screen, "Нажмите ПРОБЕЛ для продолжения", font, BLACK, 50, 350)
    elif game_state == "result":
        stats = (f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  "
                 f"Поддержка: {player.support}  Экономика: {player.economy}  "
                 f"Технологии: {player.tech}  Мораль: {player.morale}  Решения: {player.decisions}  "
                 f"Италия: {player.relations['Italy']}  Япония: {player.relations['Japan']}  Нейтралы: {player.relations['Neutral']}")
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy, player.tech, player.morale]) else BLACK,
                  50, 50, 700)
        goals_text = "Цели: " + ", ".join([f"{goal['description']} [{'✓' if goal['completed'] else ' '}]" for goal in player.goals.values()])
        draw_text(screen, goals_text, small_font, BLACK, 50, 100, 700)
        y = 150
        for line in result_text:
            y += draw_text(screen, line, small_font, BLACK, 50, y, 700)
        draw_text(screen, "Нажмите ПРОБЕЛ для продолжения, S для сохранения", font, BLACK, 50, y + 50)
    elif game_state == "game_over":
        draw_text(screen, "Игра окончена", font, BLACK, 50, 50)
        # Концовка определяется в main.py
        draw_text(screen, player.ending_text, font, BLACK, 50, 100, 900)
        stats = (f"Решения: {player.decisions}, Успешные миссии: {player.successful_missions}, "
                 f"Год: {player.year}, Технологии: {player.tech}, Мораль: {player.morale}, "
                 f"Италия: {player.relations['Italy']}, Япония: {player.relations['Japan']}")
        draw_text(screen, stats, font, BLACK, 50, 200, 900)
        goals_text = "Цели: " + ", ".join([f"{goal['description']} [{'✓' if goal['completed'] else ' '}]" for goal in player.goals.values()])
        draw_text(screen, goals_text, small_font, BLACK, 50, 300, 900)
        draw_text(screen, "Нажмите R для перезапуска", font, BLACK, 50, 350)

    if debug_mode:
        debug_info = f"State: {game_state}, Mission: {current_mission['text'] if current_mission else 'None'}"
        draw_text(screen, debug_info, small_font, BLACK, 10, screen.get_height() - 50, 980)

    pygame.display.flip()