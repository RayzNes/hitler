import random

events = [
    {"text": "Шпионы противника украли планы. Поддержка падает.", "effect": {"support": -20, "tech": -10, "morale": -5}, "region": None, "region_change": 0, "relations_change": {"Neutral": -5}, "choices": [], "follow_up": None},
    {"text": "Неожиданная поставка топлива с захваченных территорий.", "effect": {"fuel": 30, "morale": 5}, "region": "africa", "region_change": 10, "relations_change": {}, "choices": [], "follow_up": None},
    {"text": "Экономический спад: казна истощается.", "effect": {"economy": -25, "morale": -10}, "region": None, "region_change": 0, "relations_change": {"Neutral": -10}, "choices": [], "follow_up": "crisis_1" if random.random() < 0.5 else None},
    {"text": "Успешная пропаганда: население сплачивается.", "effect": {"support": 20, "morale": 10}, "region": None, "region_change": 0, "relations_change": {}, "choices": [], "follow_up": "propaganda_distrust"},
    {"text": "Дезертирство в армии: потери личного состава.", "effect": {"army": -20, "morale": -15}, "region": None, "region_change": 0, "relations_change": {"Italy": -5}, "choices": [], "follow_up": None},
    {"text": "Прорыв в тылу: дополнительные ресурсы.", "effect": {"economy": 20, "fuel": 10, "tech": 5}, "region": "east", "region_change": 5, "relations_change": {}, "choices": [], "follow_up": None},
    {"text": "Праздник победы: армия воодушевлена.", "effect": {"morale": 20, "support": 10}, "region": None, "region_change": 0, "relations_change": {"Italy": 5, "Japan": 5}, "choices": [], "follow_up": None},
    {"text": "Технологический прорыв: новые разработки.", "effect": {"tech": 20, "morale": 5}, "region": None, "region_change": 0, "relations_change": {}, "choices": [], "follow_up": None},
    # Цепочка "Экономический кризис"
    {"text": "Голод в городах: экономический кризис усиливается.", "effect": {"support": -20, "economy": -15}, "region": None, "region_change": 0, "relations_change": {"Neutral": -10}, "choices": [], "follow_up": "crisis_2", "id": "crisis_1"},
    {"text": "Бунты: народ требует реформ.", "effect": {"support": -25, "morale": -10}, "region": None, "region_change": 0, "relations_change": {"Neutral": -15}, "choices": [], "follow_up": "crisis_3", "id": "crisis_2"},
    {"text": "Чрезвычайное положение: порядок восстановлен ценой свобод.", "effect": {"support": -30, "morale": -15, "army": -10}, "region": None, "region_change": 0, "relations_change": {"Neutral": -20}, "choices": [], "follow_up": None, "id": "crisis_3"},
    # Последствие пропаганды
    {"text": "Пропаганда вызвала недоверие: народ сомневается в лидере.", "effect": {"support": -20, "morale": -5}, "region": None, "region_change": 0, "relations_change": {}, "choices": [], "follow_up": None, "id": "propaganda_distrust"},
    # Персонализированные события с выборами
    {"text": "Генерал Роммель требует больше топлива для Африканского корпуса.", "effect": {}, "region": "africa", "region_change": 0, "relations_change": {}, "choices": [
        {"text": "Дать топливо", "effect": {"fuel": -20, "army": 10, "morale": 5}, "relations_change": {"Italy": 10}},
        {"text": "Отказать", "effect": {"support": -10, "morale": -5}, "relations_change": {"Italy": -10}}
    ], "follow_up": None},
    {"text": "Шпион предлагает саботаж британских поставок.", "effect": {}, "region": None, "region_change": 0, "relations_change": {}, "choices": [
        {"text": "Рискнуть", "success_chance": 0.6, "effect": {"support": 20, "tech": 10}, "relations_change": {"Neutral": -10}},
        {"text": "Отказаться", "effect": {"support": -5}, "relations_change": {}}
    ], "follow_up": None}
]

def get_event(history, player):
    # Проверяем цепочки событий
    if player.economy < 30 and "crisis_3" not in player.event_history:
        # Запускаем или продолжаем цепочку экономического кризиса
        for event in events:
            if event.get("id") == "crisis_1" and "crisis_1" not in player.event_history:
                return event
            elif event.get("id") == "crisis_2" and "crisis_1" in player.event_history and "crisis_2" not in player.event_history:
                return event
            elif event.get("id") == "crisis_3" and "crisis_2" in player.event_history:
                return event

    # Проверяем последствия пропаганды
    if "Усилить пропаганду" in history and player.turns_since_propaganda >= 2:
        for event in events:
            if event.get("id") == "propaganda_distrust" and random.random() < 0.3:
                return event

    # Если игрок часто отступает, увеличиваем вероятность дезертирства
    if history.count("Отступить") >= 2:
        return events[4] if random.random() < 0.4 else random.choice(events)

    return random.choice(events)