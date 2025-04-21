import random

missions = [
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
        "text": "Топливный кризис: запасы на исходе. Как решить проблему?",
        "region": None,
        "choices": [
            {"text": "Захватить нефтяные поля", "success_chance": 0.6, "army_cost": 40, "fuel_cost": 30, "support_cost": 20, "economy_cost": 30, "tech_cost": 10, "reward": 50, "region_change": 0, "morale_change": 10, "relations_change": {"Neutral": -10}, "hint": "Высокий риск, но большая награда"},
            {"text": "Рационировать топливо", "success_chance": 0.85, "army_cost": 10, "fuel_cost": 5, "support_cost": 25, "economy_cost": 15, "tech_cost": 0, "reward": 20, "region_change": 0, "morale_change": -5, "relations_change": {}, "hint": "Безопасно, но малая выгода"},
            {"text": "Заключить сделку", "success_chance": 0.7, "army_cost": 5, "fuel_cost": 10, "support_cost": 30, "economy_cost": 20, "tech_cost": 5, "reward": 30, "region_change": 0, "morale_change": 0, "relations_change": {"Neutral": 10}, "hint": "Зависит от дипломатии, средний риск"}
        ]
    },
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
        "text": "Разработка нового оружия: как распределить ресурсы?",
        "region": None,
        "choices": [
            {"text": "Финансировать проект V-2", "success_chance": 0.5, "army_cost": 10, "fuel_cost": 30, "support_cost": 20, "economy_cost": 40, "tech_cost": 20, "reward": 50, "region_change": 0, "morale_change": 10, "relations_change": {}, "hint": "Прорывной потенциал, но высокая цена"},
            {"text": "Улучшить танки", "success_chance": 0.7, "army_cost": 30, "fuel_cost": 20, "support_cost": 10, "economy_cost": 20, "tech_cost": 10, "reward": 30, "region_change": 0, "morale_change": 5, "relations_change": {}, "hint": "Надежно для фронта, умеренные затраты"},
            {"text": "Отказаться от проектов", "success_chance": 0.9, "army_cost": 5, "fuel_cost": 5, "support_cost": 30, "economy_cost": 10, "tech_cost": 0, "reward": 10, "region_change": 0, "morale_change": -5, "relations_change": {}, "hint": "Сохраняет ресурсы, но теряет преимущество"}
        ]
    },
    {
        "text": "Дипломатический кризис: союзники требуют поддержки. Как поступить?",
        "region": "west",
        "choices": [
            {"text": "Отправить войска", "success_chance": 0.65, "army_cost": 35, "fuel_cost": 25, "support_cost": 15, "economy_cost": 20, "tech_cost": 5, "reward": 40, "region_change": 10, "morale_change": 5, "relations_change": {"Italy": 20, "Japan": 10}, "hint": "Укрепляет альянс, но ослабляет фронт"},
            {"text": "Предложить ресурсы", "success_chance": 0.8, "army_cost": 10, "fuel_cost": 15, "support_cost": 20, "economy_cost": 30, "tech_cost": 0, "reward": 30, "region_change": 5, "morale_change": 0, "relations_change": {"Italy": 10}, "hint": "Сохраняет армию, но истощает казну"},
            {"text": "Игнорировать требования", "success_chance": 0.7, "army_cost": 5, "fuel_cost": 5, "support_cost": 35, "economy_cost": 10, "tech_cost": 0, "reward": 20, "region_change": -15, "morale_change": -5, "relations_change": {"Italy": -20, "Japan": -10}, "hint": "Риск утраты доверия союзников"}
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
        "text": "Шпионаж: отправить агентов для саботажа врага. Какой план?",
        "region": None,
        "choices": [
            {"text": "Саботаж заводов", "success_chance": 0.6, "army_cost": 10, "fuel_cost": 10, "support_cost": 10, "economy_cost": 20, "tech_cost": 15, "reward": 40, "region_change": 0, "morale_change": 5, "relations_change": {"Neutral": -10}, "hint": "Урон врагу, но риск провала"},
            {"text": "Кража технологий", "success_chance": 0.5, "army_cost": 5, "fuel_cost": 5, "support_cost": 15, "economy_cost": 25, "tech_cost": 20, "reward": 50, "region_change": 0, "morale_change": 0, "relations_change": {"Neutral": -15}, "hint": "Большая награда, высокий риск"},
            {"text": "Отказаться от операции", "success_chance": 0.9, "army_cost": 0, "fuel_cost": 0, "support_cost": 20, "economy_cost": 5, "tech_cost": 0, "reward": 10, "region_change": 0, "morale_change": -5, "relations_change": {}, "hint": "Безопасно, но теряется шанс"}
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

def get_mission(history, player):
    # Если игрок часто подавляет протесты, увеличиваем вероятность миссий с беспорядками
    if history.count("Подавить протесты") >= 2:
        return missions[2] if random.random() < 0.5 else random.choice(missions)
    # Если экономика низкая, увеличиваем вероятность миссии по бомбоубежищам
    if player.economy < 50 and not player.bomb_shelters_built:
        return missions[7] if random.random() < 0.3 else random.choice(missions)
    return random.choice(missions)

def adjust_success_chance(mission, player):
    """Корректирует шанс успеха миссии на основе морали армии."""
    for choice in mission["choices"]:
        choice["success_chance"] = min(0.95, max(0.05, choice["success_chance"] + player.morale * 0.001))