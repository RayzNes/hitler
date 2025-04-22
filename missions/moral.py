moral_missions = [
    {
        "text": "Экономический спад: нужны рабочие руки. Как поступить?",
        "region": None,
        "choices": [
            {
                "text": "Использовать принудительный труд",
                "success_chance": 0.8,
                "army_cost": 10,
                "fuel_cost": 10,
                "support_cost": 20,
                "economy_cost": 15,
                "tech_cost": 0,
                "reward": 40,
                "region_change": 0,
                "morale_change": -10,
                "reputation_change": -20,
                "relations_change": {"Neutral": -20},
                "hint": "Увеличивает экономику, но снижает репутацию"
            },
            {
                "text": "Стимулировать добровольный труд",
                "success_chance": 0.6,
                "army_cost": 5,
                "fuel_cost": 5,
                "support_cost": 15,
                "economy_cost": 30,
                "tech_cost": 5,
                "reward": 20,
                "region_change": 0,
                "morale_change": 5,
                "reputation_change": 10,
                "relations_change": {"Neutral": 10},
                "hint": "Улучшает репутацию, но дорого"
            },
            {
                "text": "Игнорировать проблему",
                "success_chance": 0.9,
                "army_cost": 5,
                "fuel_cost": 5,
                "support_cost": 25,
                "economy_cost": 10,
                "tech_cost": 0,
                "reward": 10,
                "region_change": 0,
                "morale_change": -5,
                "reputation_change": -5,
                "relations_change": {"Neutral": -5},
                "hint": "Экономит ресурсы, но теряется поддержка"
            }
        ]
    }
]