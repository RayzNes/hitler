import json
import platform
import os

# Проверяем, работаем ли в Pyodide
IS_PYODIDE = platform.system() == "Emscripten"

if IS_PYODIDE:
    import js

def save_game(player, autosave=False):
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
        "turns_since_propaganda": player.turns_since_propaganda,
        "bomb_shelters_built": player.bomb_shelters_built,
        "goals": player.goals,
        "ending_text": getattr(player, "ending_text", "")
    }
    try:
        if IS_PYODIDE:
            if js.window.localStorage:
                key = "game_autosave" if autosave else "game_save"
                js.window.localStorage.setItem(key, json.dumps(player_data))
                return True
        else:
            filename = "game_autosave.json" if autosave else "game_save.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(player_data, f, ensure_ascii=False)
                return True
    except Exception as e:
        print(f"Ошибка сохранения: {e}")
        return False
    return False

def load_game(autosave=False):
    """Загружает состояние игрока."""
    try:
        if IS_PYODIDE:
            if js.window.localStorage:
                key = "game_autosave" if autosave else "game_save"
                if js.window.localStorage.getItem(key):
                    player_data = json.loads(js.window.localStorage.getItem(key))
                    from player import Player
                    player = Player()
                    player.__dict__.update(player_data)
                    return player
        else:
            filename = "game_autosave.json" if autosave else "game_save.json"
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    player_data = json.load(f)
                    from player import Player
                    player = Player()
                    player.__dict__.update(player_data)
                    return player
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return None
    return None