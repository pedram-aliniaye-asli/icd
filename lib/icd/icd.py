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

import screen
import keys
import utils
import signals

# Main function to start the directory navigation
def main():
    # Call initial setup function
    utils.setup()

    while True:
        key_input = keys.wait_for_key_presses() # Wait for user input
        dirs = utils.check_input(key_input, utils.load_dir_data('working_address'), utils.load_dir_data('depth_point'), utils.load_dir_data('current_dir_index')) # Process the input
        utils.save_dir_data(working_address = dirs['working_address'])
        if dirs['final_result']: # If a new directory is selected, change to it
            print(f'\n{dirs['final_result']}', end='\n')
            break
        screen.print_path_string(dirs['working_address'], dirs['current_loc_index'], dirs['dirs_list'], dirs['depth_point']) # Update the path display
        utils.save_dir_data(current_dir_index=dirs['current_loc_index'])
        utils.save_dir_data(depth_point=dirs['depth_point'])

if __name__ == "__main__":
    main()
