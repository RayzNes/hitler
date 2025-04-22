military_missions = [
    {
        "text": "Восточный фронт: армия нуждается в подкреплении. Как действовать?",
        "region": "east",
        "choices": [
            {"text": "Отправить резервы", "success_chance": 0.7, "army_cost": 30, "fuel_cost": 20, "support_cost": 10, "economy_cost": 20, "tech_cost": 5, "reward": 30, "region_change": 10, "morale_change": 5, "relations_change": {"Italy": 5}, "hint": "Риск потерь армии, но укрепляет фронт"},
            {"text": "Усилить оборону", "success_chance": 0.8, "army_cost": 20, "fuel_cost": 10, "support_cost": 15, "economy_cost": 10, "tech_cost": 0, "reward": 20, "region_change": 5, "morale_change": 0, "relations_change": {}, "hint": "Сохраняет силы, но ограничивает прогресс"},
            {"text": "Отступить", "success_chance": 0.9, "army_cost": 10, "fuel_cost": 5, "support_cost": 30, "economy_cost": 5, "tech_cost": 0, "reward": 10, "region_change": -20, "morale_change": -10, "relations_change": {"Japan": -5}, "hint": "Минимальные потери, но теряется поддержка"}
        ]
    },
    {
        "text": "Контрнаступление врага: нужно срочно укрепить позиции. Ваш план?",
        "region": "east",
        "choices": [
            {"text": "Мобилизовать резервы", "success_chance": 0.6, "army_cost": 40, "fuel_cost": 20, "support_cost": 15, "economy_cost": 25, "tech_cost": 10, "reward": 45, "region_change": 15, "morale_change": 10, "relations_change": {"Japan": 5}, "hint": "Быстрое реагирование, но большие потери"},
            {"text": "Укрепить тыл", "success_chance": 0.8, "army_cost": 20, "fuel_cost": 10, "support_cost": 20, "economy_cost": 15, "tech_cost": 5, "reward": 25, "region_change": 5, "morale_change": 0, "relations_change": {}, "hint": "Стабильность, но меньший прогресс"},
            {"text": "Контратаковать", "success_chance": 0.5, "army_cost": 50, "fuel_cost": 30, "support_cost": 10, "economy_cost": 30, "tech_cost": 15, "reward": 60, "region_change": 20, "morale_change": 15, "relations_change": {"Italy": 10}, "hint": "Высокий риск, высокая награда"}
        ]
    },
    {
        "text": "Атлантический конвой: враг атакует наши поставки. Как защитить?",
        "region": "atlantic",
        "choices": [
            {"text": "Усилить эскорт", "success_chance": 0.7, "army_cost": 20, "fuel_cost": 30, "support_cost": 10, "economy_cost": 15, "tech_cost": 5, "reward": 35, "region_change": 10, "morale_change": 5, "relations_change": {"Italy": 5}, "hint": "Сохраняет поставки, но требует топлива"},
            {"text": "Атаковать порты врага", "success_chance": 0.5, "army_cost": 30, "fuel_cost": 40, "support_cost": 15, "economy_cost": 20, "tech_cost": 10, "reward": 50, "region_change": 15, "morale_change": 10, "relations_change": {"Neutral": -10}, "hint": "Высокий риск, но большой эффект"},
            {"text": "Сократить конвои", "success_chance": 0.9, "army_cost": 5, "fuel_cost": 10, "support_cost": 20, "economy_cost": 10, "tech_cost": 0, "reward": 15, "region_change": -10, "morale_change": -5, "relations_change": {}, "hint": "Экономит ресурсы, но теряется контроль"}
        ]
    },
    {
        "text": "Партизаны атакуют тыловые линии. Как реагировать?",
        "region": "balkans",
        "choices": [
            {"text": "Отправить карательные отряды", "success_chance": 0.6, "army_cost": 30, "fuel_cost": 10, "support_cost": 20, "economy_cost": 15, "tech_cost": 0, "reward": 30, "region_change": 5, "morale_change": -10, "relations_change": {"Neutral": -15}, "hint": "Восстанавливает контроль, но ухудшает репутацию"},
            {"text": "Предложить амнистию", "success_chance": 0.7, "army_cost": 10, "fuel_cost": 5, "support_cost": 25, "economy_cost": 20, "tech_cost": 5, "reward": 20, "region_change": 0, "morale_change": 5, "relations_change": {"Neutral": 10}, "hint": "Снижает напряжение, но требует ресурсов"},
            {"text": "Игнорировать угрозу", "success_chance": 0.9, "army_cost": 5, "fuel_cost": 5, "support_cost": 30, "economy_cost": 10, "tech_cost": 0, "reward": 10, "region_change": -10, "morale_change": -5, "relations_change": {}, "hint": "Экономит силы, но теряется контроль"}
        ]
    }
]