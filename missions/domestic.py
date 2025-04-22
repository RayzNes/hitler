domestic_missions = [
    {
        "text": "Внутренние беспорядки: поддержка падает. Как восстановить контроль?",
        "region": None,
        "choices": [
            {"text": "Усилить пропаганду", "success_chance": 0.75, "army_cost": 10, "fuel_cost": 5, "support_cost": 20, "economy_cost": 25, "tech_cost": 10, "reward": 40, "region_change": 0, "morale_change": 5, "relations_change": {}, "hint": "Эффективно, но дорого"},
            {"text": "Раздать ресурсы", "success_chance": 0.8, "army_cost": 15, "fuel_cost": 20, "support_cost": 10, "economy_cost": 30, "tech_cost": 0, "reward": 30, "region_change": 0, "morale_change": 0, "relations_change": {}, "hint": "Снижает напряжение, но истощает казну"},
            {"text": "Подавить протесты", "success_chance": 0.5, "army_cost": 30, "fuel_cost": 10, "support_cost": 40, "economy_cost": 20, "tech_cost": 0, "reward": 50, "region_change": 0, "morale_change": -15, "relations_change": {"Neutral": -15}, "hint": "Рискованно, но может восстановить порядок"}
        ]
    },
    {
        "text": "Подготовка к бомбардировкам: союзники усиливают авиацию. Как защититься?",
        "region": None,
        "choices": [
            {"text": "Построить бомбоубежища", "success_chance": 0.8, "army_cost": 10, "fuel_cost": 10, "support_cost": 10, "economy_cost": 30, "tech_cost": 10, "reward": 20, "region_change": 0, "morale_change": 5, "relations_change": {}, "hint": "Защищает от бомбардировок, но дорого"},
            {"text": "Усилить ПВО", "success_chance": 0.6, "army_cost": 20, "fuel_cost": 15, "support_cost": 15, "economy_cost": 20, "tech_cost": 15, "reward": 30, "region_change": 0, "morale_change": 0, "relations_change": {}, "hint": "Снижает урон, но требует технологий"},
            {"text": "Игнорировать угрозу", "success_chance": 0.9, "army_cost": 5, "fuel_cost": 5, "support_cost": 20, "economy_cost": 5, "tech_cost": 0, "reward": 10, "region_change": 0, "morale_change": -5, "relations_change": {"Neutral": -5}, "hint": "Экономит ресурсы, но риск катастрофы"}
        ]
    }
]