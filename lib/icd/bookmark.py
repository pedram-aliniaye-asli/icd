# ==============================================================================
# Copyright (c) 2025 Pedram Aliniaye Asli
#
# This software is released under the MIT License.
# See the LICENSE file for more details.
#
# This software is provided 'as-is', without any express or implied warranty. In no event will the authors be held
# liable for any damages arising from the use of this software.
#
# You are free to modify and distribute this code under the terms of the MIT License,
# as long as you refer to the original author.
# ==============================================================================
import json
import os
import screen


BOOKMARK_FILE = os.path.join(os.path.expanduser("~"), ".local", "share", "icd", "bookmarks.json")

# Function to save a directory path with a user-given name.
def save_bookmark(directory):
    name = input("\n Enter a name for the bookmark: ").strip()
    if not name:
        screen.print_output("Bookmark name cannot be empty.")
        return

    bookmarks = {}
    if os.path.exists(BOOKMARK_FILE):
        with open(BOOKMARK_FILE, "r") as file:
            try:
                bookmarks = json.load(file)
            except json.JSONDecodeError:
                pass  # Ignore corrupt JSON file

    bookmarks[name] = directory

    os.makedirs(os.path.dirname(BOOKMARK_FILE), exist_ok=True)
    with open(BOOKMARK_FILE, "w") as file:
        json.dump(bookmarks, file, indent=4)

    screen.print_output(f"Bookmark '{name}' saved.")

# Function to load a directory path using a user-given name.
def load_bookmark():
    screen.print_output("\n Enter the bookmark name to load: ")
    name = input().strip()

    if os.path.exists(BOOKMARK_FILE):
        with open(BOOKMARK_FILE, "r") as file:
            bookmarks = json.load(file)

        if name in bookmarks:
            return {'working_address' : bookmarks[name], 'current_loc_index' : len(bookmarks[name]) - 1, 'depth_point' : 0}
            
        else:
            screen.print_output("Bookmark not found.")
    else:
        screen.print_output("No bookmarks saved yet.")

    return None
