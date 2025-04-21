import random

events = [
    {"text": "Шпионы противника украли планы. Поддержка падает.", "effect": {"support": -20, "tech": -10, "morale": -5}, "region": None, "region_change": 0},
    {"text": "Неожиданная поставка топлива с захваченных территорий.", "effect": {"fuel": 30, "morale": 5}, "region": "africa", "region_change": 10},
    {"text": "Экономический спад: казна истощается.", "effect": {"economy": -25, "morale": -10}, "region": None, "region_change": 0},
    {"text": "Успешная пропаганда: население сплачивается.", "effect": {"support": 20, "morale": 10}, "region": None, "region_change": 0},
    {"text": "Дезертирство в армии: потери личного состава.", "effect": {"army": -20, "morale": -15}, "region": None, "region_change": 0},
    {"text": "Прорыв в тылу: дополнительные ресурсы.", "effect": {"economy": 20, "fuel": 10, "tech": 5}, "region": "east", "region_change": 5},
    {"text": "Праздник победы: армия воодушевлена.", "effect": {"morale": 20, "support": 10}, "region": None, "region_change": 0},
    {"text": "Технологический прорыв: новые разработки.", "effect": {"tech": 20, "morale": 5}, "region": None, "region_change": 0}
]

def get_event(history):
    # Если игрок часто отступает, увеличиваем вероятность дезертирства
    if history.count("Отступить") >= 2:
        return events[4] if random.random() < 0.4 else random.choice(events)
    return random.choice(events)