import json

def load_data(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(file_path, data):
    with open(file_path, mode = 'w', encoding = 'utf-8') as file:
        json.dump(data, file, indent = 4)