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

class CountTracker:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {"num_printed_lines": 0}  # Dictionary to store values
        return cls._instance

    def get_value(self, key):
        """Returns the stored value for the given key."""
        return self._data.get(key, None)

    def set_value(self, key, value):
        """Sets a new value for the given key."""
        if isinstance(value, int) and value >= 0:
            self._data[key] = value
        else:
            raise ValueError("Value must be a non-negative integer")

    def increment_value(self, key, count=1):
        """Increments the value of a given key by the specified count."""
        if isinstance(count, int) and count > 0:
            self._data[key] = self._data.get(key, 0) + count
        else:
            raise ValueError("Increment count must be a positive integer")

    def reset_value(self, key):
        """Resets the value of a given key to zero."""
        if key in self._data:
            self._data[key] = 0

    def get_all_values(self):
        """Returns all stored values as a dictionary."""
        return self._data.copy()

class DirsAddress:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {'working_address': [], 'current_dir_index': 0, 'depth_point': 0}
            # working_address -> Store the current working full address
            # current_dir_index -> Store the index of current directory in the working address list
            # depth_point -> Store the focus point in list of child directories
        return cls._instance
    
    def get_value(self, key):
        """Returns the stored value for the given key."""
        return self._data.get(key, None)

    def set_value(self, key, value):
        """Sets a new value for the given key."""
        self._data[key] = value

    def get_all_values(self):
        """Returns all stored values as a dictionary."""
        return self._data.copy()
