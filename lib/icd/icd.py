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

import os
import sys
import tty
import termios
import shutil
import signal

# Function to handle Ctrl+C interruptions
def handle_ctrl_c(signum, frame):
    print("\nExiting...", flush=True)  
    sys.exit(0)

# Register signal handler to catch Ctrl+C
signal.signal(signal.SIGINT, handle_ctrl_c)

# Function to retrieve the list of directories in a given path
def get_dir_list(address, dir_index):
    if dir_index == 0:
        dir = '/'
    else:
        dir = "/".join(address[:dir_index+1])
    dirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))] # List only directories
    return dirs

# Function to print the current working directory in a user-friendly format
def print_working_directory():
    current_dir = os.getcwd()
    print(current_dir[:current_dir.find(os.path.basename(current_dir))] + f'[{os.path.basename(current_dir)}]', end="", flush=True)

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
    # print("\n", end="", flush=True)
    # print(">>>>>", end="", flush=True)

    while True:
        key = get_key()
        
        if key == '\x1b':  # Escape key, start of an arrow key sequence
            next_key = get_key()  # Read next character
            if next_key == '[':
                arrow_key = get_key()  # Read the last character in the arrow key sequence
                print("\r\033[K", end="", flush=True)  # Clear the line first
                if arrow_key == 'A':
                    return 'U' # Up arrow
                elif arrow_key == 'B':
                    return 'D' # Down arrow
                elif arrow_key == 'C':
                    return 'R' # Right arrow
                elif arrow_key == 'D':
                    return 'L' # Left arrow
        elif key == '\n':  # Enter key
            return 'Enter'

# Function to handle user input and update the directory navigation based on that input       
def check_input(key_input, address, depth_point, current_loc_index):
    global working_add
    dirs_list = get_dir_list(address, current_loc_index)
    final_result = None
    if key_input == 'R': # Move right
        if depth_point > 0:
            new_current_loc = get_dir_list(address, current_loc_index)[depth_point-1]
            address = address[:current_loc_index+1]
            address.append(new_current_loc)
            current_loc_index += 1
        elif depth_point == 0:
            if current_loc_index < len(address) - 1:
                current_loc_index += 1
        dirs_list = get_dir_list(address, current_loc_index)
        depth_point = 0
    elif key_input == 'L': # Move left
        address_line = "/".join(address)
        if current_loc_index > 0:
            current_loc_index -= 1
        if len(address_line) >= shutil.get_terminal_size().columns:
            address = address[:current_loc_index+1]
        dirs_list = get_dir_list(address, current_loc_index)
        depth_point = 0
    dirs_list.insert(0, '.') # Add the current directory (.) to the list
    if key_input == 'U': # Move up
        if depth_point <= 0:
            depth_point = 0
        else:
            depth_point -= 1
    elif key_input == 'D': # Move down
        if depth_point >= len(dirs_list)-1:
            depth_point = len(dirs_list)-1
        else:
            depth_point += 1
    if key_input == 'Enter': # Enter a directory
        final_result = change_directory(address, current_loc_index, dirs_list, depth_point)
    working_add = address
    return (dirs_list, current_loc_index, depth_point, final_result)

# Function to print the current directory path with visual indicators
def print_path_string(address,current_dir_index, next_list, depth_point, input_list):
    global lines_to_delete
    current_dir = address[current_dir_index]
    path_string = ("/".join(address[:current_dir_index]) + f'/[{address[current_dir_index]}]/' + "/".join(address[current_dir_index+1:])).rstrip('/') # Build the full path string
    extra_chars = len(path_string) - shutil.get_terminal_size().columns 
    if extra_chars > 0: # Check if the path is too long for the terminal
        path_string = '...' + path_string[-(2*extra_chars):] # Truncate the path if it's too long
    if input_list[0]:
        delete_lines(input_list) # Delete previous output lines
    else:
        input_list[0] = True
    print(path_string, end="\n", flush=True)
    for index,item in enumerate(next_list): # Print directories in the current folder
        print(f'[{"*" if index == depth_point else " "}]',item, end="\n", flush=True)
    lines_to_delete[1] = address
    lines_to_delete[2] = next_list

# Function to change the current directory based on user input
def change_directory(working_add, current_dir_index, dirs_list, depth_point):
    final_add = "/".join(working_add[:current_dir_index]) + f'/{working_add[current_dir_index]}' + f'/{dirs_list[depth_point]}'
    if os.path.isdir(final_add): # If the directory exists, returns it
        return final_add
    return None

# Function to delete previous lines in the terminal to keep the output clean
def delete_lines(input_list):
    terminal_width = shutil.get_terminal_size().columns
    for line in input_list[2]: # Loop through the lines to delete
        print('\r', end="") # Return to the starting position
        print(" " * (terminal_width - 2), end = " ") # Clear the line
        print('\033[F', end="") # Move the cursor up one line
    print('\033[F', end="")
    print(" " * (terminal_width - 2) , end = " ")
    print("\r", end="")

# Global variables
lines_to_delete = [False, [], []]# Store information about lines to delete: lines_to_delete = [True/False, working_add, next_list]
working_add = [] # Store the current working directory

# Main function to start the directory navigation
def main():
    print_working_directory() # Display the initial working directory
    global working_add
    working_add = os.getcwd().split('/') # Convert the current working directory into a list of folders
    current_dir = os.path.basename(os.getcwd()) # Get the name of the current directory
    current_dir_index = working_add.index(current_dir)
    global lines_to_delete
    depth_point = 0 # Start at the top of the directory list
    while True:
        key_input = wait_for_key_presses() # Wait for user input
        dirs = check_input(key_input, working_add, depth_point, current_dir_index) # Process the input
        if dirs[3]: # If a new directory is selected, change to it
            print(dirs[3])
            break
        print_path_string(working_add, dirs[1], dirs[0], dirs[2], lines_to_delete) # Update the path display
        depth_point = dirs[2] # Update the depth point
        current_dir_index = dirs[1] # Update the current directory index
if __name__ == "__main__":
    main()
