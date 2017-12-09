"""
Toy Robot Simulator
Module - Move Robot
"""

def move_robot(position, board_bounds):
    """
    Move robot around the board

    Parameters
    ----------
    position : List
        Robots current position on the board

    board_bounds: range
        Range of board

    Returns
    -------
    List
        New position if successful, None otherwise
    """
    new_position = [position['x'], position['y'], position['f']]

    if position['f'] == 'north' and int(position['y']) + 1 in board_bounds:
        new_position[1] = int(position['y']) + 1

    elif position['f'] == 'south' and int(position['y']) - 1 in board_bounds:
        new_position[1] = int(position['y']) - 1

    elif position['f'] == 'west' and int(position['x']) - 1 in board_bounds:
        new_position[0] = int(position['x']) - 1

    elif position['f'] == 'east' and int(position['x']) + 1 in board_bounds:
        new_position[0] = int(position['x']) + 1

    else:
        new_position = None
        print('Movement not allowed')

    return new_position
