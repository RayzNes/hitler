import random
from .military import military_missions
from .technology import technology_missions
from .domestic import domestic_missions
from .diplomatic import diplomatic_missions
from .economic import economic_missions
from .espionage import espionage_missions

all_missions = (
    military_missions +
    technology_missions +
    domestic_missions +
    diplomatic_missions +
    economic_missions +
    espionage_missions
)

def get_mission(history, player):
    # Если игрок часто подавляет протесты, увеличиваем вероятность миссий с беспорядками
    if history.count("Подавить протесты") >= 2:
        return domestic_missions[0] if random.random() < 0.5 else random.choice(all_missions)
    # Если экономика низкая, увеличиваем вероятность миссии по бомбоубежищам
    if player.economy < 50 and not player.bomb_shelters_built:
        return domestic_missions[1] if random.random() < 0.3 else random.choice(all_missions)
    # Если регион Балканы под угрозой, увеличиваем вероятность партизанской миссии
    if player.regions["balkans"] < 30:
        return military_missions[3] if random.random() < 0.4 else random.choice(all_missions)
    return random.choice(all_missions)

def adjust_success_chance(mission, player):
    """Корректирует шанс успеха миссии на основе морали армии."""
    for choice in mission["choices"]:
        choice["success_chance"] = min(0.95, max(0.05, choice["success_chance"] + player.morale * 0.001))