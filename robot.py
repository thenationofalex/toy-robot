"""
Toy Robot Simulator
Version 1.0.0
"""

from modules.validateplace import validate_place
from modules.orientate import orientate_robot
from modules.move import move_robot

class Robot(object):
    """Toy Robot Simulator"""

    def __init__(self):
        """Set base parameters"""
        self.board_bounds = range(5)
        self.position = {'x': 0, 'y': 0, 'f': 'north'}

    def __update_position(self, new_position):
        self.position['x'] = new_position[0]
        self.position['y'] = new_position[1]
        self.position['f'] = new_position[2]

    def __announce_position(self):
        """Announce position of the robot"""
        print('x=' + str(self.position['x']) + ', y=' + \
              str(self.position['y']) + ', f=' + str(self.position['f']) + '\n')

    @classmethod
    def menu(cls):
        """Return cli menu"""
        return print('Available commands:\n- PLACE X, Y, F\n- MOVE\n- LEFT\n- RIGHT\n- REPORT\n- EXIT\n\n')

    def main(self):
        """Start robot simulator"""
        print('Toy Robot Simulator\n')
        start_command = None

        while start_command is None:
            start_command = validate_place(
                input('Please enter a starting position (place X,Y,F):\n\n'),
                self.board_bounds
            )
            if start_command is not None:
                self.__update_position(start_command)
                self.menu()

        while True:
            command = input().lower()

            if command == 'move':
                move = move_robot(self.position, self.board_bounds)
                if move:
                    self.__update_position(move)

            elif command == 'left' or command == 'right':
                self.position['f'] = orientate_robot(command, self.position['f'])

            elif command == 'report':
                self.__announce_position()

            elif 'place' in command:
                update_place = validate_place(command, self.board_bounds)
                self.__update_position(update_place)

            elif command == 'exit':
                break
            else:
                print('Invalid command')

PROGRAM = Robot()
PROGRAM.main()
