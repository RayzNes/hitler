import random
from .military import military_missions
from .technology import technology_missions
from .domestic import domestic_missions
from .diplomatic import diplomatic_missions
from .economic import economic_missions
from .espionage import espionage_missions
from .investment import investment_missions
from .moral import moral_missions

all_missions = (
    military_missions +
    technology_missions +
    domestic_missions +
    diplomatic_missions +
    economic_missions +
    espionage_missions +
    investment_missions +
    moral_missions
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
    # Если экономика высокая, увеличиваем вероятность инвестиций
    if player.economy > 70:
        return investment_missions[0] if random.random() < 0.3 else random.choice(all_missions)
    # Если репутация низкая, увеличиваем вероятность моральных дилемм
    if player.reputation < 30:
        return moral_missions[0] if random.random() < 0.3 else random.choice(all_missions)
    return random.choice(all_missions)

def adjust_success_chance(mission, player):
    """Корректирует шанс успеха миссии на основе морали армии и лидеров."""
    for choice in mission["choices"]:
        base_chance = choice["success_chance"]
        # Учет морали
        base_chance = min(0.95, max(0.05, base_chance + player.morale * 0.001))
        # Учет лидеров
        if mission["region"] == "africa" and player.leaders["Rommel"]["active"]:
            base_chance = min(0.95, base_chance + player.leaders["Rommel"]["bonus"]["africa_mission_success"])
        if mission["region"] == "east" and player.leaders["Guderian"]["active"]:
            base_chance = min(0.95, base_chance + player.leaders["Guderian"]["bonus"]["east_mission_success"])
        choice["success_chance"] = base_chance