"""
Toy Robot Simulator
Module - Input Controller
"""

from modules.validateplace import validate_place
from modules.orientate import orientate_robot
from modules.move import move_robot

def __announce_position(position):
    """
    Announce position of the robot

    Parameters
    ----------
    position : Dict
        Robots current position on the board

    Returns
    -------
    Str
        Formatted string of robots position on the board

    """
    return print('x=' + str(position['x']) + ', y=' + \
            str(position['y']) + ', f=' + str(position['f']) + '\n')

def command_menu():
    """Return cli menu"""
    return print('Available commands:\n- PLACE X, Y, F\n- MOVE\n- LEFT\n- RIGHT\n- REPORT\n- EXIT\n\n')

def start_command():
    """Issue start command"""
    return 'Please enter a starting position (place X,Y,F):\n\n'

def input_controller(command, position, board_bounds):
    """
    Process input

    Parameters
    ----------
    command : str
        Command for robot

    position : Dict
        Robots current position on the board

    board_bounds: range
        Range of board

    Returns
    -------
    List
        New position if successful, None otherwise or
        exits the program if `exit` is recieved.

    """
    if command == 'move':
        move = move_robot(position, board_bounds)
        if move:
            return move

    elif command == 'left' or command == 'right':
        return orientate_robot(command, position)

    elif command == 'report':
        return __announce_position(position)

    elif 'place' in command:
        return validate_place(command, board_bounds)

    elif command == 'exit':
        quit()
    else:
        print('Invalid command')
