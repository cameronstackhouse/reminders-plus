"""
Module containing functions to read and processing settings
stored in the program json file "settings.json"
"""

import json

def get_settings(filename: str):
    """
    
    """

    file = open(filename)
    data = json.load(file)
    
    file.close()

    return data["Name"], data["Fontsize"], data["Window_x"], data["Window_y"]

if __name__ == "__main__":
    name, fontsize, window_x, window_y = get_settings("settings.json")
    

