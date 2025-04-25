import json

def load_json_objects(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
