investment_missions = [
    {
        "text": "Долгосрочные инвестиции: в какой проект вложить ресурсы?",
        "region": None,
        "choices": [
            {
                "text": "Восстановить экономику",
                "success_chance": 0.8,
                "army_cost": 10,
                "fuel_cost": 10,
                "support_cost": 10,
                "economy_cost": 50,
                "tech_cost": 5,
                "reward": 0,
                "region_change": 0,
                "morale_change": 5,
                "relations_change": {"Neutral": 5},
                "investment": {"type": "Economy Recovery", "turns_left": 3, "effect": {"economy": 20}},
                "hint": "Через 3 хода: Экономика +20"
            },
            {
                "text": "Укрепить ПВО",
                "success_chance": 0.7,
                "army_cost": 15,
                "fuel_cost": 15,
                "support_cost": 10,
                "economy_cost": 30,
                "tech_cost": 15,
                "reward": 0,
                "region_change": 0,
                "morale_change": 5,
                "relations_change": {},
                "investment": {"type": "AA Defense", "turns_left": 3, "effect": {"tech": 15, "morale": 5}},
                "hint": "Через 3 хода: Технологии +15, Мораль +5"
            },
            {
                "text": "Отказаться от инвестиций",
                "success_chance": 0.9,
                "army_cost": 5,
                "fuel_cost": 5,
                "support_cost": 15,
                "economy_cost": 10,
                "tech_cost": 0,
                "reward": 10,
                "region_change": 0,
                "morale_change": -5,
                "relations_change": {},
                "investment": None,
                "hint": "Экономит ресурсы, но теряет возможности"
            }
        ]
    }
]