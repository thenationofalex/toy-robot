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

    IndexError
        If command isn't valid return False

    """
    command = command.lower().split()
    error_message = 'Error please enter a valid command'

    if len(command) != 2:
        print(error_message)
        return None

    place = command[1].split(',')

    try:
        int(place[0])
    except ValueError:
        return None

    try:
        int(place[1])
    except ValueError:
        return None

    if command[0] != 'place':
        print(error_message)
        return None

    elif int(place[0]) not in board_bounds and \
         int(place[1]) not in board_bounds:
        print('Error please enter a value between 0 & 4')
        return None

    elif place[2] != 'north' and place[2] != 'south' \
         and place[2] != 'east' and place[2] != 'west':
        print('Error with starting position F. Please enter either NORTH, SOUTH, WEST or EAST')
        return None

    else:
        return [place[0], place[1], place[2]]
