military_events = [
    {
        "text": "Дезертирство в армии: потери личного состава.",
        "effect": {"army": -20, "morale": -15},
        "region": None,
        "region_change": 0,
        "relations_change": {"Italy": -5},
        "choices": [],
        "follow_up": None
    },
    {
        "text": "Суровая зима парализует Восточный фронт. Солдаты страдают от холода.",
        "effect": {"army": -15, "morale": -10},
        "region": "east",
        "region_change": -5,
        "relations_change": {},
        "choices": [
            {"text": "Поставить обогреватели", "effect": {"fuel": -20, "morale": 10, "army": 5}, "relations_change": {}},
            {"text": "Продолжать наступление", "effect": {"army": -10, "morale": -5}, "relations_change": {"Japan": -5}}
        ],
        "follow_up": None
    }
]