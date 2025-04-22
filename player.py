# Модуль для управления состоянием игрока в игре "Кризис Командования"
class Player:
    def __init__(self):
        """Инициализация игрока с начальными ресурсами и статистикой."""
        self.army = 100  # Состояние армии
        self.fuel = 100  # Запасы топлива
        self.support = 100  # Поддержка населения/элиты
        self.economy = 100  # Финансовые ресурсы
        self.tech = 50  # Технологический прогресс
        self.morale = 50  # Мораль армии
        self.reputation = 50  # Репутация (влияет на дипломатию и моральные выборы)
        self.decisions = 0  # Количество принятых решений
        self.successful_missions = 0  # Количество успешных миссий
        self.consecutive_successes = 0  # Серия успешных миссий для бонусов
        self.year = 1943  # Текущий год в игре
        self.history = []  # История выборов игрока
        self.regions = {"east": 100, "west": 50, "africa": 20, "atlantic": 30, "balkans": 40}  # Контроль регионов (%)
        self.relations = {"Italy": 50, "Japan": 50, "Neutral": 20}  # Отношения с союзниками
        self.event_history = []  # История событий для цепочек
        self.turns_since_propaganda = float('inf')  # Счётчик ходов с последнего использования пропаганды
        self.bomb_shelters_built = False  # Построены ли бомбоубежища
        self.investments = []  # Список долгосрочных инвестиций: [{"type": str, "turns_left": int, "effect": dict}]
        self.leaders = {
            "Rommel": {"active": True, "bonus": {"africa_mission_success": 0.1}},
            "Guderian": {"active": True, "bonus": {"east_mission_success": 0.1}},
            "Speer": {"active": True, "bonus": {"economy_cost_reduction": 0.1}}
        }
        self.goals = {  # Долгосрочные цели
            "hold_east_1945": {"description": "Удержать Восточный фронт до 1945 года", "completed": False},
            "develop_v2": {"description": "Разработать V-2", "completed": False},
            "high_support_1944": {"description": "Сохранить поддержку выше 70 в 1944 году", "completed": False}
        }

    def is_alive(self):
        """Проверка, может ли игрок продолжать игру."""
        return (self.army > 0 and self.fuel > 0 and self.support > 0 and
                self.economy > 0 and self.morale > 0)