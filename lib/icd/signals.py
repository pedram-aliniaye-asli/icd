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
import signal

# Function to handle Ctrl+C interruptions
def handle_ctrl_c(signum, frame):
    print("\nExiting...", flush=True)
    sys.stdout.flush()  
    sys.exit(0)

# Register signal handler to catch Ctrl+C
signal.signal(signal.SIGINT, handle_ctrl_c)
