diplomatic_missions = [
    {
        "text": "Дипломатический кризис: союзники требуют поддержки. Как поступить?",
        "region": "west",
        "choices": [
            {"text": "Отправить войска", "success_chance": 0.65, "army_cost": 35, "fuel_cost": 25, "support_cost": 15, "economy_cost": 20, "tech_cost": 5, "reward": 40, "region_change": 10, "morale_change": 5, "relations_change": {"Italy": 20, "Japan": 10}, "hint": "Укрепляет альянс, но ослабляет фронт"},
            {"text": "Предложить ресурсы", "success_chance": 0.8, "army_cost": 10, "fuel_cost": 15, "support_cost": 20, "economy_cost": 30, "tech_cost": 0, "reward": 30, "region_change": 5, "morale_change": 0, "relations_change": {"Italy": 10}, "hint": "Сохраняет армию, но истощает казну"},
            {"text": "Игнорировать требования", "success_chance": 0.7, "army_cost": 5, "fuel_cost": 5, "support_cost": 35, "economy_cost": 10, "tech_cost": 0, "reward": 20, "region_change": -15, "morale_change": -5, "relations_change": {"Italy": -20, "Japan": -10}, "hint": "Риск утраты доверия союзников"}
        ]
    }
]