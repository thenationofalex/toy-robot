"""
Toy Robot Simulator
Module - Validate Place
"""

def validate_place(command, board_bounds):
    """
    Validate robots position

    Parameters
    ----------
    command : str
        Command from users input

    board_bounds: range
        Range of board

    Returns
    -------
    List
        Position if successful, None otherwise

    Raises
    ------
    ValueError
        If the first or second item in the list isn't an integer
        return False

    """
    valid = None
    command = command.lower().split()

    if len(command) != 2:
        valid = None

    place = command[1].split(',')

    try:
        int(place[0])
    except ValueError:
        valid = None

    try:
        int(place[1])
    except ValueError:
        valid = None

    if command[0] != 'place':
        print('Error please enter a valid command')
        valid = None
    elif int(place[0]) not in board_bounds and \
         int(place[1]) not in board_bounds:
        print('Error please enter a value between 0 & 4')
        valid = None
    elif place[2] != 'north' and place[2] != 'south' \
         and place[2] != 'east' and place[2] != 'west':
        print('Error with starting position F. Please enter either NORTH, SOUTH, WEST or EAST')
        valid = None
    else:
        valid = [place[0], place[1], place[2]]

    return valid
