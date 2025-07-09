# state_manager.py

import json
import os
from config import STATE_FILE

def load_state():
    """Load the last processed row index (0-based) from JSON state file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            data = json.load(f)
            return data.get("last_row", -1)
    return -1

def save_state(last_row):
    """Save the last processed row index to JSON state file."""
    with open(STATE_FILE, 'w') as f:
        json.dump({"last_row": last_row}, f, indent=2)
