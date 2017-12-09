"""
Toy Robot Simulator
Version 0.0.1
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

    def announce_position(self):
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
                move = move_robot(self.position, self.board_bounds)
                if move:
                    self.position['x'] = move[0]
                    self.position['y'] = move[1]
                    self.position['f'] = move[2]

            elif command == 'left' or command == 'right':
                self.position['f'] = orientate_robot(command, self.position['f'])

            elif command == 'report':
                self.announce_position()

            elif 'place' in command:
                update_place = validate_place(command, self.board_bounds)
                self.position['x'] = update_place[0]
                self.position['y'] = update_place[1]
                self.position['f'] = update_place[2]
                
            elif command == 'exit':
                break
            else:
                print('Invalid command')


PROGRAM = Robot()
PROGRAM.main()
