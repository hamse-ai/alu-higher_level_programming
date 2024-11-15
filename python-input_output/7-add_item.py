#!/usr/bin/python3
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# File name where the list will be saved
filename = "add_item.json"

try:
    # Try to load existing items from file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # If file doesn't exist, start with empty list
    items = []

# Add all command line arguments (excluding script name) to the list
items.extend(sys.argv[1:])

# Save updated list back to file
save_to_json_file(items, filename)
