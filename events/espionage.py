import random

espionage_events = [
    {
        "text": "Шпионы противника украли планы. Поддержка падает.",
        "effect": {"support": -20, "tech": -10, "morale": -5},
        "region": None,
        "region_change": 0,
        "relations_change": {"Neutral": -5},
        "choices": [],
        "follow_up": None
    },
    {
        "text": "Шпион предлагает саботаж британских поставок.",
        "effect": {},
        "region": None,
        "region_change": 0,
        "relations_change": {},
        "choices": [
            {"text": "Рискнуть", "success_chance": 0.6, "effect": {"support": 20, "tech": 10}, "relations_change": {"Neutral": -10}},
            {"text": "Отказаться", "effect": {"support": -5}, "relations_change": {}}
        ],
        "follow_up": "counterintelligence" if random.random() < 0.4 else None
    },
    {
        "text": "Враг усилил контрразведку: шпионская сеть под угрозой.",
        "effect": {"tech": -15, "support": -10},
        "region": None,
        "region_change": 0,
        "relations_change": {"Neutral": -5},
        "choices": [],
        "follow_up": None,
        "id": "counterintelligence"
    }
]