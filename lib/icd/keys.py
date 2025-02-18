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

import sys
import tty
import termios

# Function to read a single key press from the user (without blocking program)
def get_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)  # Save the current terminal settings
    try:
        tty.setcbreak(fd)  # Set the terminal to cbreak mode (no buffering)
        key = sys.stdin.read(1)  # Read one key press
        return key
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # Restore original settings

# Function to continuously listen for key presses and handle special keys (e.g., arrow keys)
def wait_for_key_presses():
    while True:
        key = get_key()
        
        if key == '\x1b':  # Escape key, start of an arrow key sequence
            next_key = get_key()  # Read next character
            if next_key == '[':
                arrow_key = get_key()  # Read the last character in the arrow key sequence
                # print("\r\033[K", end="", flush=True)  # Clear the line first
                if arrow_key == 'A':
                    return 'Up' # Up arrow
                elif arrow_key == 'B':
                    return 'Down' # Down arrow
                elif arrow_key == 'C':
                    return 'Right' # Right arrow
                elif arrow_key == 'D':
                    return 'Left' # Left arrow
        elif key == '\n':  # Enter key
            return 'Enter'
        elif key == '\x14':  # ASCII for Ctrl+T
            return 'Tree_View'
        elif key == '\x02':  # ASCII for Ctrl+B
            return 'Load_Bookmark'
        elif key == '\x04':  # ASCII for Ctrl+D
            return 'Save_Bookmark'
