import os
import json

STATE_FILE = 'cloudflex_state.json'

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_state(state):
    with open(STATE_FILE, 'w') as file:
        json.dump(state, file, indent=4)