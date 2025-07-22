import json

def load_config(config_path='config.json'):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config