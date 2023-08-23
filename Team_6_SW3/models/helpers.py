# Define a function to determine friends and enemies based on color
def get_friends_and_enemies(colour, white_locations, black_locations):
    if colour == 'white':
        return white_locations, black_locations
    else:
        return black_locations, white_locations
