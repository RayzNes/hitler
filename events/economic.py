import  random

economic_events = [
    {
        "text": "Экономический спад: казна истощается.",
        "effect": {"economy": -25, "morale": -10},
        "region": None,
        "region_change": 0,
        "relations_change": {"Neutral": -10},
        "choices": [],
        "follow_up": "crisis_1" if random.random() < 0.5 else None
    },
    {
        "text": "Голод в городах: экономический кризис усиливается.",
        "effect": {"support": -20, "economy": -15},
        "region": None,
        "region_change": 0,
        "relations_change": {"Neutral": -10},
        "choices": [],
        "follow_up": "crisis_2",
        "id": "crisis_1"
    },
    {
        "text": "Бунты: народ требует реформ.",
        "effect": {"support": -25, "morale": -10},
        "region": None,
        "region_change": 0,
        "relations_change": {"Neutral": -15},
        "choices": [],
        "follow_up": "crisis_3",
        "id": "crisis_2"
    },
    {
        "text": "Чрезвычайное положение: порядок восстановлен ценой свобод.",
        "effect": {"support": -30, "morale": -15, "army": -10},
        "region": None,
        "region_change": 0,
        "relations_change": {"Neutral": -20},
        "choices": [],
        "follow_up": None,
        "id": "crisis_3"
    }
]