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
    bool
        True if successful, False otherwise

    Raises
    ------
    ValueError
        If the first or second item in the list isn't an integer
        return False

    """
    valid = True
    command = command.lower().split()

    if len(command) != 2:
        valid = False

    place = command[1].split(',')

    try:
        int(place[0])
    except ValueError:
        valid = False

    try:
        int(place[1])
    except ValueError:
        valid = False

    if command[0] != 'place':
        print('Error please enter a valid command')
        valid = False
    elif int(place[0]) not in board_bounds and \
         int(place[1]) not in board_bounds:
        print('Error please enter a value between 0 & 4')
        valid = False
    elif place[2] != 'north' and place[2] != 'south' \
         and place[2] != 'east' and place[2] != 'west':
        print('Error with starting position F. Please enter either NORTH, SOUTH, WEST or EAST')
        valid = False

    return valid
