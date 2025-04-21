import random

missions = [
    {
        "text": "Восточный фронт: армия нуждается в подкреплении. Как действовать?",
        "choices": [
            {"text": "Отправить резервы", "success_chance": 0.7, "army_cost": 30, "fuel_cost": 20, "support_cost": 10, "economy_cost": 20, "reward": 30, "hint": "Риск потерь армии, но укрепляет фронт"},
            {"text": "Усилить оборону", "success_chance": 0.8, "army_cost": 20, "fuel_cost": 10, "support_cost": 15, "economy_cost": 10, "reward": 20, "hint": "Сохраняет силы, но ограничивает прогресс"},
            {"text": "Отступить", "success_chance": 0.9, "army_cost": 10, "fuel_cost": 5, "support_cost": 30, "economy_cost": 5, "reward": 10, "hint": "Минимальные потери, но теряется поддержка"}
        ]
    },
    {
        "text": "Топливный кризис: запасы на исходе. Как решить проблему?",
        "choices": [
            {"text": "Захватить нефтяные поля", "success_chance": 0.6, "army_cost": 40, "fuel_cost": 30, "support_cost": 20, "economy_cost": 30, "reward": 50, "hint": "Высокий риск, но большая награда"},
            {"text": "Рационировать топливо", "success_chance": 0.85, "army_cost": 10, "fuel_cost": 5, "support_cost": 25, "economy_cost": 15, "reward": 20, "hint": "Безопасно, но малая выгода"},
            {"text": "Заключить сделку", "success_chance": 0.7, "army_cost": 5, "fuel_cost": 10, "support_cost": 30, "economy_cost": 20, "reward": 30, "hint": "Зависит от дипломатии, средний риск"}
        ]
    },
    {
        "text": "Внутренние беспорядки: поддержка падает. Как восстановить контроль?",
        "choices": [
            {"text": "Усилить пропаганду", "success_chance": 0.75, "army_cost": 10, "fuel_cost": 5, "support_cost": 20, "economy_cost": 25, "reward": 40, "hint": "Эффективно, но дорого"},
            {"text": "Раздать ресурсы", "success_chance": 0.8, "army_cost": 15, "fuel_cost": 20, "support_cost": 10, "economy_cost": 30, "reward": 30, "hint": "Снижает напряжение, но истощает казну"},
            {"text": "Подавить протесты", "success_chance": 0.5, "army_cost": 30, "fuel_cost": 10, "support_cost": 40, "economy_cost": 20, "reward": 50, "hint": "Рискованно, но может восстановить порядок"}
        ]
    },
    {
        "text": "Разработка нового оружия: как распределить ресурсы?",
        "choices": [
            {"text": "Финансировать проект V-2", "success_chance": 0.5, "army_cost": 10, "fuel_cost": 30, "support_cost": 20, "economy_cost": 40, "reward": 50, "hint": "Прорывной потенциал, но высокая цена"},
            {"text": "Улучшить танки", "success_chance": 0.7, "army_cost": 30, "fuel_cost": 20, "support_cost": 10, "economy_cost": 20, "reward": 30, "hint": "Надежно для фронта, умеренные затраты"},
            {"text": "Отказаться от проектов", "success_chance": 0.9, "army_cost": 5, "fuel_cost": 5, "support_cost": 30, "economy_cost": 10, "reward": 10, "hint": "Сохраняет ресурсы, но теряет преимущество"}
        ]
    },
    {
        "text": "Дипломатический кризис: союзники требуют поддержки. Как поступить?",
        "choices": [
            {"text": "Отправить войска", "success_chance": 0.65, "army_cost": 35, "fuel_cost": 25, "support_cost": 15, "economy_cost": 20, "reward": 40, "hint": "Укрепляет альянс, но ослабляет фронт"},
            {"text": "Предложить ресурсы", "success_chance": 0.8, "army_cost": 10, "fuel_cost": 15, "support_cost": 20, "economy_cost": 30, "reward": 30, "hint": "Сохраняет армию, но истощает казну"},
            {"text": "Игнорировать требования", "success_chance": 0.7, "army_cost": 5, "fuel_cost": 5, "support_cost": 35, "economy_cost": 10, "reward": 20, "hint": "Риск утраты доверия союзников"}
        ]
    },
    {
        "text": "Контрнаступление врага: нужно срочно укрепить позиции. Ваш план?",
        "choices": [
            {"text": "Мобилизовать резервы", "success_chance": 0.6, "army_cost": 40, "fuel_cost": 20, "support_cost": 15, "economy_cost": 25, "reward": 45, "hint": "Быстрое реагирование, но большие потери"},
            {"text": "Укрепить тыл", "success_chance": 0.8, "army_cost": 20, "fuel_cost": 10, "support_cost": 20, "economy_cost": 15, "reward": 25, "hint": "Стабильность, но меньший прогресс"},
            {"text": "Контратаковать", "success_chance": 0.5, "army_cost": 50, "fuel_cost": 30, "support_cost": 10, "economy_cost": 30, "reward": 60, "hint": "Высокий риск, высокая награда"}
        ]
    }
]

def get_mission(history):
    # Если игрок часто подавляет протесты, увеличиваем вероятность миссий с беспорядками
    if history.count("Подавить протесты") >= 2:
        return missions[2] if random.random() < 0.5 else random.choice(missions)
    return random.choice(missions)