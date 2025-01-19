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

#!/bin/bash

# Enable exit on error
set -e

# Variables
BASH_SCRIPT="bin/icd"
PYTHON_SCRIPT="lib/icd/icd.py"
COMMAND_NAME="icd"
BASH_SCRIPT_DEST="/usr/local/bin/icd"
PYTHON_SCRIPT_DEST="/usr/local/lib/icd/icd.py"
ALIAS_COMMAND="alias $COMMAND_NAME='source $BASH_SCRIPT_DEST'"

# Check if the BASH_SCRIPT file exists
if [[ ! -f "$BASH_SCRIPT" ]]; then
    echo "Error: $BASH_SCRIPT not found."
    exit 1
fi

# Check if the PYTHON_SCRIPT file exists
if [[ ! -f "$PYTHON_SCRIPT" ]]; then
    echo "Error: $PYTHON_SCRIPT not found."
    exit 1
fi
sudo -v 
# Copy the bash script to /usr/local/bin and make it executable
echo "Copying bash script..."
if ! sudo cp "$BASH_SCRIPT" "$BASH_SCRIPT_DEST"; then
    echo "Error: Failed to copy $BASH_SCRIPT to $BASH_SCRIPT_DEST."
    exit 1
fi
sudo chmod +x "$BASH_SCRIPT_DEST"

# Copy the Python script to /usr/local/lib and create the directory if needed
echo "Copying Python script..."
if ! sudo mkdir -p /usr/local/lib/icd/ || ! sudo cp "$PYTHON_SCRIPT" "$PYTHON_SCRIPT_DEST"; then
    echo "Error: Failed to copy $PYTHON_SCRIPT to $PYTHON_SCRIPT_DEST."
    exit 1
fi

# Add the alias to the shell configuration file if it doesn't exist
if ! grep -Fxq "$ALIAS_COMMAND" ~/.bashrc; then
    echo "Adding alias to ~/.bashrc..."
    echo "$ALIAS_COMMAND" >> ~/.bashrc
fi

# Reload shell configuration
echo "Reloading shell configuration..."
source ~/.bashrc

# Print installation complete message
echo "Installation complete. You can now use '$COMMAND_NAME' to ride through your directories!"
