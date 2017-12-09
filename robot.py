"""
Toy Robot Simulator
Version 0.0.1
"""

from modules.validateplace import validate_place
from modules.orientate import orientate_robot

class Robot(object):
    """Toy Robot Simulator"""

    def __init__(self):
        """Set base parameters"""
        self.board_bounds = range(5)
        self.position = {'x': 0, 'y': 0, 'f': 'n'}

    def announce_position(self):
        """Announce position of the robot"""
        print('x=' + str(self.position['x']) + ', y=' + \
              str(self.position['y']) + ', f=' + str(self.position['f']) + '\n')

    def move_robot(self):
        """Move the robot
            If robot is facing north or south move along the X axis
            Else move along the Y axis
        """
        move_error = False

        if self.position['f'] == 'north' and int(self.position['y']) + 1 in self.board_bounds:
            self.position['y'] = int(self.position['y']) + 1

        elif self.position['f'] == 'south' and int(self.position['y']) - 1 in self.board_bounds:
            self.position['y'] = int(self.position['y']) - 1

        elif self.position['f'] == 'west' and int(self.position['x']) - 1 in self.board_bounds:
            self.position['x'] = int(self.position['x']) - 1

        elif self.position['f'] == 'east' and int(self.position['x']) + 1 in self.board_bounds:
            self.position['x'] = int(self.position['x']) + 1

        else:
            move_error = True

        return move_error

    @classmethod
    def menu(cls):
        """Return cli menu"""
        return print('Available commands:\n- PLACE X, Y, F\n- MOVE\n- LEFT\n- RIGHT\n- REPORT\n- EXIT\n\n')

    def main(self):
        """Start robot simulator"""
        print('Toy Robot Simulator\n')
        start_command = False

        while start_command is False:
            start_command = validate_place(
                input('Please enter a starting position (place X,Y,F):\n\n'),
                self.board_bounds
            )

        self.position['x'] = start_command[0]
        self.position['y'] = start_command[1]
        self.position['f'] = start_command[2]
        self.menu()

        while True:
            command = input().lower()

            if command == 'move':
                move = self.move_robot()
                if move:
                    print('Movement not allowed')
            elif command == 'left' or command == 'right':
                self.position['f'] = orientate_robot(command, self.position['f'])
            elif command == 'report':
                self.announce_position()
            elif 'place' in command:
                validate_place(command, self.board_bounds)
            elif command == 'exit':
                break
            else:
                print('Invalid command')


PROGRAM = Robot()
PROGRAM.main()
