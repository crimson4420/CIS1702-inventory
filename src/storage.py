#handles the loading and saving of the inventory data to a JSON file
#all file I/O is isolated here to keep the rest of the program clean

import json
import os
from typing import List, Dict, Any

DATA_FILE = os.path.join("data", "inventory.json")


def load_inventory(path: str = DATA_FILE) -> List[Dict[str, Any]]:
    #loads the inventory from the json file, returns an empty list if missing or invalid
    try:
        if not os.path.exists(path):
            return []

        # If the file exists but is empty, treat as no data
        if os.path.getsize(path) == 0:
            return []

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Ensure the JSON is a list in the expected format
        if isinstance(data, list):
            return data

        # If someone saved the wrong JSON shape, fail safely
        return []

    except (OSError, json.JSONDecodeError):
        # OSError covers file permission and path issues
        # JSONDecodeError covers broken json file
        return []


def save_inventory(inventory: List[Dict[str, Any]], path: str = DATA_FILE) -> bool:
    #saves the inventory to a json file, returns True if successful, else False
    try:
        # Makes sure the data folder exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(inventory, f, indent=2)

        return True

    except OSError:
        return False