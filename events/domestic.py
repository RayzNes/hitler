domestic_events = [
    {
        "text": "Успешная пропаганда: население сплачивается.",
        "effect": {"support": 20, "morale": 10},
        "region": None,
        "region_change": 0,
        "relations_change": {},
        "choices": [],
        "follow_up": "propaganda_distrust"
    },
    {
        "text": "Пропаганда вызвала недоверие: народ сомневается в лидере.",
        "effect": {"support": -20, "morale": -5},
        "region": None,
        "region_change": 0,
        "relations_change": {},
        "choices": [],
        "follow_up": None,
        "id": "propaganda_distrust"
    },
    {
        "text": "Гуманитарный кризис: население требует продовольствия.",
        "effect": {},
        "region": None,
        "region_change": 0,
        "relations_change": {},
        "choices": [
            {"text": "Раздать продовольствие", "effect": {"economy": -20, "support": 15, "morale": 5}, "relations_change": {"Neutral": 10}},
            {"text": "Приоритет армии", "effect": {"support": -15, "morale": -10, "army": 10}, "relations_change": {"Neutral": -10}}
        ],
        "follow_up": None
    }
]