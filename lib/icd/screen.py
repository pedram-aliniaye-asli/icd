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

import shutil
import shared_info


def print_output(msg, ending=""):
    # line_count = msg.count('\n')
    # if ending == '\n':
    #     line_count += 1
    print(msg, end=ending, flush=True)
    num_printed_lines = shared_info.CountTracker()
    # num_printed_lines.increment_value("num_printed_lines", line_count + 1)
    num_printed_lines.increment_value("num_printed_lines", 1)

def delete_lines(number_of_lines):
    # terminal_width = shutil.get_terminal_size().columns  # Get terminal width
    # Loop to delete lines
    for i in range(number_of_lines):  # Loop exactly `number_of_lines` times
        # print("\r" + " " * terminal_width, end="\r")  # Clear current line & reset cursor
        print("\r\033[K", end="", flush=True)  # Clear the line first
        if i < number_of_lines -1:  # Only move up if it's not the last line
            print("\033[F", end="")  # Move the cursor up one line

# Function to print the current directory path with visual indicators
def print_path_string(address,current_dir_index, next_list, depth_point):#error list index out of range
    path_string = ("/".join(address[:current_dir_index]) + f'/[{address[current_dir_index]}]/' + "/".join(address[current_dir_index+1:])).rstrip('/') # Build the full path string
    extra_chars = len(path_string) - shutil.get_terminal_size().columns 
    if extra_chars > 0: # Check if the path is too long for the terminal
        path_string = '...' + path_string[-(2*extra_chars):] # Truncate the path if it's too long
    nltd = shared_info.CountTracker()
    num_lines_delete = nltd.get_value('num_printed_lines')
    if num_lines_delete > 0:
        delete_lines(num_lines_delete) # Delete previous output lines
        nltd.reset_value("num_printed_lines") # Reset line count after operation
    print_output(path_string, ending="\n")
    for index,item in enumerate(next_list): # Print directories in the current folder
        if index == len(next_list)-1:
            print_output(f'[{"*" if index == depth_point else " "}] {item}', ending="")
        else:
            print_output(f'[{"*" if index == depth_point else " "}] {item}', ending="\n")
