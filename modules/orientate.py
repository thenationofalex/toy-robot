"""
Toy Robot Simulator
Module - Orientate
"""

def orientate_robot(direction, position):
    """
    Orientate the robot

    Parameters
    ----------
    direction : str
        Direction to orientate the robot left or right

    position : List
        Position of robot

    Returns
    -------
    Dict
        Update position of the robot

    """
    compass = ['north', 'south', 'east', 'west']
    current_position = compass.index(position['f'])

    if direction == 'right':
        if current_position == 0:
            position['f'] = compass[2]
        elif current_position == 1:
            position['f'] = compass[3]
        elif  current_position == 2:
            position['f'] = compass[1]
        elif current_position == 3:
            position['f'] = compass[0]
    elif direction == 'left':
        if current_position == 0:
            position['f'] = compass[3]
        elif current_position == 1:
            position['f'] = compass[2]
        elif  current_position == 2:
            position['f'] = compass[0]
        elif current_position == 3:
            position['f'] = compass[1]

    return position
