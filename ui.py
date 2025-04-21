import pygame

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)

# Переменные для шрифтов
font = None
small_font = None


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


def render_game_state(screen, game_state, player, current_mission, current_event, choices, result_text, debug_mode):
    screen.fill(GRAY)

    if game_state == "start":
        draw_text(screen, "Кризис Командования", font, BLACK, 50, 50)
        draw_text(screen, "1943 год. Вы стоите во главе Германии в разгар войны. Ваши решения определят судьбу.",
                  small_font, BLACK, 50, 150, 700)
        draw_text(screen, "Нажмите ПРОБЕЛ для начала или L для загрузки", font, BLACK, 50, 300)
    elif game_state == "mission":
        stats = f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  Поддержка: {player.support}  Экономика: {player.economy}  Решения: {player.decisions}"
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy]) else BLACK, 50,
                  50, 700)
        draw_text(screen, "Новая миссия начинается...", small_font, BLACK, 50, 150, 700)
        draw_text(screen, current_mission["text"], small_font, BLACK, 50, 200, 700)
        draw_text(screen, "Нажмите ПРОБЕЛ для продолжения", font, BLACK, 50, 350)
    elif game_state == "choice":
        stats = f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  Поддержка: {player.support}  Экономика: {player.economy}  Решения: {player.decisions}"
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy]) else BLACK, 50,
                  50, 700)
        draw_text(screen, current_mission["text"], small_font, BLACK, 50, 150, 700)
        for i, choice in enumerate(choices):
            draw_text(screen, f"{i + 1}. {choice['text']} ({choice['hint']})", small_font, BLACK, 50, 250 + i * 50, 700)
        draw_text(screen, "Нажмите 1, 2 или 3 для выбора, S для сохранения", font, BLACK, 50, 450)
    elif game_state == "result":
        stats = f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  Поддержка: {player.support}  Экономика: {player.economy}  Решения: {player.decisions}"
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy]) else BLACK, 50,
                  50, 700)
        y = 150
        for line in result_text:
            y += draw_text(screen, line, small_font, BLACK, 50, y, 700)
        draw_text(screen, "Нажмите ПРОБЕЛ для продолжения, S для сохранения", font, BLACK, 50, y + 50)
    elif game_state == "event":
        stats = f"Год: {player.year}  Армия: {player.army}  Топливо: {player.fuel}  Поддержка: {player.support}  Экономика: {player.economy}  Решения: {player.decisions}"
        draw_text(screen, stats, font,
                  RED if any(v < 30 for v in [player.army, player.fuel, player.support, player.economy]) else BLACK, 50,
                  50, 700)
        draw_text(screen, "Событие!", small_font, BLACK, 50, 150, 700)
        draw_text(screen, current_event["text"], small_font, BLACK, 50, 200, 700)
        draw_text(screen, "Нажмите ПРОБЕЛ для продолжения", font, BLACK, 50, 350)
    elif game_state == "game_over":
        draw_text(screen, "Игра окончена", font, BLACK, 50, 50)
        ending_text = (
            "Раннее поражение: Германия пала в 1943." if player.year == 1943 else
            "Вы продержались до 1944, но силы иссякли." if player.year == 1944 else
            "Удержание позиций до 1945: редкий успех."
        )
        draw_text(screen, ending_text, font, BLACK, 50, 100)
        stats = f"Решения: {player.decisions}, Успешные миссии: {player.successful_missions}, Год: {player.year}"
        draw_text(screen, stats, font, BLACK, 50, 150)
        draw_text(screen, "Нажмите R для перезапуска", font, BLACK, 50, 250)

    if debug_mode:
        debug_info = f"State: {game_state}, Mission: {current_mission['text'] if current_mission else 'None'}"
        draw_text(screen, debug_info, small_font, BLACK, 10, HEIGHT - 50, 780)

    pygame.display.flip()