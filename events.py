import random

events = [
    {"text": "Шпионы противника украли планы. Поддержка падает.", "effect": {"support": -20}},
    {"text": "Неожиданная поставка топлива с захваченных территорий.", "effect": {"fuel": 30}},
    {"text": "Экономический спад: казна истощается.", "effect": {"economy": -25}},
    {"text": "Успешная пропаганда: население сплачивается.", "effect": {"support": 20}},
    {"text": "Дезертирство в армии: потери личного состава.", "effect": {"army": -20}},
    {"text": "Прорыв в тылу: дополнительные ресурсы.", "effect": {"economy": 20, "fuel": 10}}
]

def get_event(history):
    # Если игрок часто отступает, увеличиваем вероятность дезертирства
    if history.count("Отступить") >= 2:
        return events[4] if random.random() < 0.4 else random.choice(events)
    return random.choice(events)