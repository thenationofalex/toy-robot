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
    List
        Update position of the robot

    """
    compass = ['north', 'south', 'east', 'west']
    current_position = compass.index(position['f'])
    orientation = None

    if direction == 'right':
        if current_position == 0:
            orientation = compass[2]
        elif current_position == 1:
            orientation = compass[3]
        elif  current_position == 2:
            orientation = compass[1]
        elif current_position == 3:
            orientation = compass[0]
    elif direction == 'left':
        if current_position == 0:
            orientation = compass[3]
        elif current_position == 1:
            orientation = compass[2]
        elif  current_position == 2:
            orientation = compass[0]
        elif current_position == 3:
            orientation = compass[1]

    return [position['x'], position['y'], orientation]
