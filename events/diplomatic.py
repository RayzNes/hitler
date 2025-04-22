import random

diplomatic_events = [
    {
        "text": "Италия на грани капитуляции: союзники требуют решительных действий.",
        "effect": {},
        "region": None,
        "region_change": 0,
        "relations_change": {},
        "choices": [
            {"text": "Отправить подкрепления", "effect": {"army": -20, "fuel": -15, "relations_change": {"Italy": 20}}, "success_chance": 0.7},
            {"text": "Игнорировать", "effect": {"support": -10, "relations_change": {"Italy": -30}}, "success_chance": 0.9}
        ],
        "follow_up": "italy_surrender" if random.random() < 0.3 else None,
        "id": "italy_crisis"
    },
    {
        "text": "Италия капитулировала: альянс ослаблен.",
        "effect": {"support": -20, "morale": -15, "relations_change": {"Italy": -50}},
        "region": "west",
        "region_change": -20,
        "relations_change": {"Italy": -50},
        "choices": [],
        "follow_up": None,
        "id": "italy_surrender"
    }
]