import json
from json import JSONDecodeError
from pathlib import Path

class InvalidConfigError(Exception):
    pass

essential_keys = {"mode", "database_url", "api_key"}
acceptable_modes = {"debug", "production"}

def load_config(filepath):
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        try:
            config_file = json.load(file)
        except JSONDecodeError as e:
            raise

    missing = essential_keys - config_file.keys()
    if missing:
        raise InvalidConfigError(f"Missing required config keys: {missing}")

    mode = str(config_file["mode"]).strip().lower()
    if mode not in acceptable_modes:
        raise InvalidConfigError(f"{config_file['mode']} is invalid mode")

    config_file["mode"] = mode
    return config_file

if __name__ == "__main__":
    config_path = "config.json"  

    try:
        cfg = load_config(config_path)
    except FileNotFoundError:
        print("Config file not found")
    except JSONDecodeError:
        print("Invalid JSON")
    except InvalidConfigError:
        print("Config Error")
    except Exception:
        print("Unexpected Error")
    else:
        print("Configuration loaded successfully.")
         