espionage_missions = [
    {
        "text": "Шпионаж: отправить агентов для саботажа врага. Какой план?",
        "region": None,
        "choices": [
            {"text": "Саботаж заводов", "success_chance": 0.6, "army_cost": 10, "fuel_cost": 10, "support_cost": 10, "economy_cost": 20, "tech_cost": 15, "reward": 40, "region_change": 0, "morale_change": 5, "relations_change": {"Neutral": -10}, "hint": "Урон врагу, но риск провала"},
            {"text": "Кража технологий", "success_chance": 0.5, "army_cost": 5, "fuel_cost": 5, "support_cost": 15, "economy_cost": 25, "tech_cost": 20, "reward": 50, "region_change": 0, "morale_change": 0, "relations_change": {"Neutral": -15}, "hint": "Большая награда, высокий риск"},
            {"text": "Отказаться от операции", "success_chance": 0.9, "army_cost": 0, "fuel_cost": 0, "support_cost": 20, "economy_cost": 5, "tech_cost": 0, "reward": 10, "region_change": 0, "morale_change": -5, "relations_change": {}, "hint": "Безопасно, но теряется шанс"}
        ]
    }
]