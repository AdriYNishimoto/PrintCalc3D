import json
import os

CONFIG_FILE = os.path.join("data", "config.json")
HISTORY_FILE = os.path.join("data", "history.json")

DEFAULT_CONFIG = {
    "theme": "dark",
    "printer": {
        "name": "Default Printer",
        "power_consumption_w": 350,
        "monthly_maintenance": 20.0,
        "printer_price": 2500.0,
        "lifespan_prints": 2000,
        "energy_rate": 0.85
    },
    "defaults": {
        "spool_weight_g": 1000,
        "spool_price": 120.0,
        "hourly_rate": 30.0,
        "profit_margin": 50.0
    }
}

def load_config():
    """Loads configuration from file or returns defaults."""
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return DEFAULT_CONFIG

def save_config(config):
    """Saves configuration to file."""
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def load_history():
    """Loads calculation history."""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_history(history_item):
    """Appends a new item to history."""
    history = load_history()
    history.append(history_item)
    
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=4)

def export_history_csv(filepath):
    """Exports history to CSV."""
    import csv
    history = load_history()
    if not history:
        return False
    
    try:
        keys = history[0].keys()
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, keys)
            dict_writer.writeheader()
            dict_writer.writerows(history)
        return True
    except IOError:
        return False
