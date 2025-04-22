# Константы игры
WIDTH = 1000
HEIGHT = 800
FPS = 60
EVENT_CHANCE_NORMAL = 0.3  # Вероятность обычного события для нормальной сложности
EVENT_CHANCE_EASY = 0.2   # Вероятность для легкой сложности
EVENT_CHANCE_HARD = 0.4   # Вероятность для сложной сложности
DEBUG_MODE = False  # Режим отладки

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Настройки сложности
DIFFICULTY_MODIFIERS = {
    "easy": {"resource_bonus": 20, "event_chance": EVENT_CHANCE_EASY},
    "normal": {"resource_bonus": 0, "event_chance": EVENT_CHANCE_NORMAL},
    "hard": {"resource_bonus": -20, "event_chance": EVENT_CHANCE_HARD}
}