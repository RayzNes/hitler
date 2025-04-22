import random
from .military import military_events
from .economic import economic_events
from .diplomatic import diplomatic_events
from .espionage import espionage_events
from .domestic import domestic_events
from .catastrophes import catastrophes

all_events = (
    military_events +
    economic_events +
    diplomatic_events +
    espionage_events +
    domestic_events
)

def get_event(history, player):
    # Проверяем возможность катастрофы (5% вероятность)
    if random.random() < 0.05:
        return random.choice(catastrophes)

    # Проверяем цепочки событий
    if player.economy < 30 and "crisis_3" not in player.event_history:
        for event in economic_events:
            if event.get("id") == "crisis_1" and "crisis_1" not in player.event_history:
                return event
            elif event.get("id") == "crisis_2" and "crisis_1" in player.event_history and "crisis_2" not in player.event_history:
                return event
            elif event.get("id") == "crisis_3" and "crisis_2" in player.event_history:
                return event

    # Проверяем последствия пропаганды
    if "Усилить пропаганду" in history and player.turns_since_propaganda >= 2:
        for event in domestic_events:
            if event.get("id") == "propaganda_distrust" and random.random() < 0.3:
                return event

    # Если игрок часто отступает, увеличиваем вероятность дезертирства
    if history.count("Отступить") >= 2:
        return military_events[0] if random.random() < 0.4 else random.choice(all_events)

    # Если отношения с Италией низкие, увеличиваем вероятность кризиса
    if player.relations["Italy"] < 20:
        return diplomatic_events[0] if random.random() < 0.5 else random.choice(all_events)

    return random.choice(all_events)