"""
Toy Robot Simulator
Version 1.0.0
"""

from modules.validateplace import validate_place
from modules.inputcontroller import input_controller, command_menu, start_command

class Robot(object):
    """Toy Robot Simulator"""

    def __init__(self):
        """Set base parameters"""
        self.board_bounds = range(5)
        self.position = {'x': 0, 'y': 0, 'f': 'north'}

    def __update_position(self, new_position):
        self.position['x'] = new_position['x']
        self.position['y'] = new_position['y']
        self.position['f'] = new_position['f']

    def main(self):
        """Start robot simulator"""
        print('Toy Robot Simulator v1.0.0\n')
        initial_command = None

        while initial_command is None:
            initial_command = validate_place(input(start_command()), self.board_bounds)

            if initial_command is not None:
                self.__update_position(initial_command)
                command_menu()

        while True:
            command = input_controller(input().lower(), self.position, self.board_bounds)
            if command is not False:
                self.__update_position(command)
            else:
                break

PROGRAM = Robot()
PROGRAM.main()
