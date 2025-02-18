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
import shutil
import bookmark
import tree_view
import shared_info
import sys
import screen

# Function to setup initial values
def setup():
    address_info_dict = shared_info.DirsAddress() # An instance of the shared info about address and dirs
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        working_add = sys.argv[1].rstrip('/')
        # address_info_dict.set_value('working_address', sys.argv[1].rstrip('/')) # Set current working address to directory from user input
    else:
        working_add = os.getcwd()
        # address_info_dict.set_value('working_address', os.getcwd()) # Set current working address to "Current Working Directory"
    # working_add = address_info_dict.get_value('working_address')
    screen.print_output(get_working_directory(working_add)) # Display the initial working directory
    # print(screen.get_working_directory(working_add),end="",flush=True)
    current_dir = os.path.basename(working_add) # Get the name of the current directory
    working_add = working_add.split('/') # Convert the current working directory into a list of folders
    current_dir_index = len(working_add) - 1 - working_add[::-1].index(current_dir) # Get the index of current directory from the end of the list, helping the with directories with same name
    depth_point = 0 # Start at the top of the directory list
    save_dir_data(working_address = working_add, current_dir_index = current_dir_index, depth_point = depth_point)

# Function to retrieve the list of directories in a given path
def get_dir_list(address, dir_index):
    if dir_index == 0:
        dir = '/'
    else:
        dir = "/".join(address[:dir_index+1])
    dirs = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))] # List only directories
    return dirs


# Function to handle user input and update the directory navigation based on that input       
def check_input(key_input, address, depth_point, current_loc_index):
    dirs_list = get_dir_list(address, current_loc_index)
    final_result = None
    if key_input == 'Right': # Move right
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
    elif key_input == 'Left': # Move left
        address_line = "/".join(address)
        if current_loc_index > 0:
            current_loc_index -= 1
        if len(address_line) >= shutil.get_terminal_size().columns:
            address = address[:current_loc_index+1]
        dirs_list = get_dir_list(address, current_loc_index)
        depth_point = 0
    dirs_list.insert(0, '.') # Add the current directory (.) to the list
    if key_input == 'Up': # Move up
        if depth_point <= 0:
            depth_point = 0
        else:
            depth_point -= 1
    elif key_input == 'Down': # Move down
        if depth_point >= len(dirs_list)-1:
            depth_point = len(dirs_list)-1
        else:
            depth_point += 1
    if key_input == 'Enter': # Enter a directory
        final_add = "/".join(address[:current_loc_index]) + f'/{address[current_loc_index]}' + f'/{dirs_list[depth_point]}'
        final_result = return_dest_directory(final_add)
    # elif key_input == 'Tree_View': # Show Tree View
    #     tree_view.show_tree_view(address)
    elif key_input == 'Load_Bookmark':  # Load a Bookmark
        address, current_loc_index, depth_point = bookmark.load_bookmark().values()
    elif key_input == 'Save_Bookmark':  # Save a Bookmark
        bookmark.save_bookmark(address)

    result = {'working_address':address, 'dirs_list':dirs_list, 'current_loc_index':current_loc_index, 'depth_point':depth_point, 'final_result':final_result}
    return result


# Function to return the destination directory based on user input
def return_dest_directory(final_add):
    if os.path.isdir(final_add): # If the directory exists, returns it
        return final_add
    return None


# Function to print the current working directory in a user-friendly format
def get_working_directory(address):
    # pwd = str(address[:address.find(os.path.basename(address))] + f'[{os.path.basename(address)}]')
    # return pwd
    dirname = os.path.dirname(address)  # Get the parent directory
    basename = os.path.basename(address)  # Get the last part of the path
    return os.path.join(dirname, f'[{basename}]')  # Append [basename] to the path

# Function to save data related to Directories' info
def save_dir_data(working_address = None, current_dir_index = None, depth_point = None):
    address_info_dict = shared_info.DirsAddress()
    if working_address:
        address_info_dict.set_value('working_address', working_address)
    if current_dir_index is not None:
        address_info_dict.set_value('current_dir_index', current_dir_index)
    if depth_point is not None:
        address_info_dict.set_value('depth_point', depth_point)

# Function to load data related to Directories' info
def load_dir_data(key):
    address_info_dict = shared_info.DirsAddress()
    if key in address_info_dict.get_all_values():
        return address_info_dict.get_value(key)
