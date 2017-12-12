"""
Toy Robot Simulator
Module - Move Robot
"""

def move_robot(position, board_bounds):
    """
    Move robot around the board

    Parameters
    ----------
    position : Dict
        Robots current position on the board

    board_bounds: range
        Range of board

    Returns
    -------
    Dict
        New position if successful, None otherwise
    """

    if position['f'] == 'north' and int(position['y']) + 1 in board_bounds:
        position['y'] = str(int(position['y']) + 1)

    elif position['f'] == 'south' and int(position['y']) - 1 in board_bounds:
        position['y'] = str(int(position['y']) - 1)

    elif position['f'] == 'west' and int(position['x']) - 1 in board_bounds:
        position['x'] = str(int(position['x']) - 1)

    elif position['f'] == 'east' and int(position['x']) + 1 in board_bounds:
        position['x'] = str(int(position['x']) + 1)

    else:
        print('Movement not allowed')

    return position
