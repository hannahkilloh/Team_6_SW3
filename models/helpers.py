import os

# Define a function to determine friends and enemies based on color
def get_friends_and_enemies(colour, white_locations, black_locations):
    if colour == 'white':
        return white_locations, black_locations
    else:
        return black_locations, white_locations

# this function makes sure to always load files from the root rather than working directory
# this was causing tests to fail when loading assets into pygame
def get_file_path_from_root(path_to_file):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return f"{root_path}/{path_to_file}"
