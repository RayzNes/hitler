import json
import platform
import os

# Проверяем, работаем ли в Pyodide
IS_PYODIDE = platform.system() == "Emscripten"

if IS_PYODIDE:
    import js

def save_game(player):
    """Сохраняет состояние игрока."""
    player_data = {
        "army": player.army,
        "fuel": player.fuel,
        "support": player.support,
        "economy": player.economy,
        "tech": player.tech,
        "morale": player.morale,
        "decisions": player.decisions,
        "successful_missions": player.successful_missions,
        "year": player.year,
        "history": player.history,
        "regions": player.regions,
        "relations": player.relations,
        "event_history": player.event_history,
        "turns_since_propaganda": player.turns_since_propaganda
    }
    try:
        if IS_PYODIDE:
            if js.window.localStorage:
                js.window.localStorage.setItem("game_save", json.dumps(player_data))
                return True
        else:
            with open("game_save.json", "w", encoding="utf-8") as f:
                json.dump(player_data, f, ensure_ascii=False)
                return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False
    return False

def load_game():
    """Загружает состояние игрока."""
    try:
        if IS_PYODIDE:
            if js.window.localStorage and js.window.localStorage.getItem("game_save"):
                player_data = json.loads(js.window.localStorage.getItem("game_save"))
                from player import Player
                player = Player()
                player.__dict__.update(player_data)
                return player
        else:
            if os.path.exists("game_save.json"):
                with open("game_save.json", "r", encoding="utf-8") as f:
                    player_data = json.load(f)
                    from player import Player
                    player = Player()
                    player.__dict__.update(player_data)
                    return player
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return None
    return None