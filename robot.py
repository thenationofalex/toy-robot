"""
Toy Robot Simulator
Version 0.0.0
"""

class Robot(object):
    """Toy Robot Simulator"""

    def __init__(self):
        """Set base parameters"""
        self.position = {'x': 0, 'y': 0, 'f': 'n'}
        self.board_bounds = range(0, 4)
        self.compass = ['n', 'e', 's', 'w']

    def announce_position(self):
        """Announce position of the robot"""
        if self.position['f'] == 'n':
            pos_f = 'NORTH'
        elif self.position['f'] == 's':
            pos_f = 'SOUTH'
        elif self.position['f'] == 'e':
            pos_f = 'EAST'
        elif self.position['f'] == 'w':
            pos_f = 'WEST'
        print(self.position['x'] + ',' + self.position['y'] + ',' + pos_f + '\n')

    def update_robots_position(self, pos_x=False, pos_y=False, pos_f=False):
        """Update robots position on the board"""

        self.position['x'] = pos_x if pos_x else self.position['x']
        self.position['y'] = pos_y if pos_y else self.position['y']
        self.position['f'] = pos_f if pos_f else self.position['f']
        self.announce_position()

    def validate_place(self, command):
        """Validate place command"""
        # ValueError: invalid literal for int() with base 10: ''

        if len(command) != 2:
            print('Error')
            return False

        place = command[1].split(',')

        if command[0] != 'place':
            print('Error please enter a valid command')
            return False
        elif int(place[0]) not in self.board_bounds:
            print('Error please enter a value between 0 & 4')
            return False
        elif int(place[1]) not in self.board_bounds:
            print('Error please enter a value between 0 & 4')
            return False
        elif place[2] != 'n' and place[2] != 's' and place[2] != 'e' and place[2] != 'w':
            print('Error with starting position F. Please enter either N, S, W or E')
            return False
        else:
            self.update_robots_position(place[0], place[1], place[2])
            return True

    def move_robot(self):
        """Move the robot"""
        current_position = self.compass
        pass

    def orientate_robot(self, direction):
        """Orientate the robot"""
        
        current_position = self.compass.index(self.position['f'])

        if direction == 'right':
            if current_position == 3:
                self.update_robots_position(False, False, self.compass[0])
            else:
                self.update_robots_position(False, False, self.compass[current_position + 1])
        else:
            if current_position == 0:
                self.update_robots_position(False, False, self.compass[3])
            else:
                self.update_robots_position(False, False, self.compass[current_position - 1])

    @classmethod
    def menu(cls):
        """Return cli menu"""
        return print('Available commands:\nPLACE X, Y, F\nMOVE\nLEFT\nRIGHT\nREPORT\n\n')

    def main(self):
        """Start robot simulator"""
        print('🤖 Toy Robot Simulator\n')
        start_command = False

        while start_command is False:
            start_command = self.validate_place(
                input('Please enter a starting position:\n\n').lower().split()
            )

        self.menu()

        while True:
            command = input().lower()

            if command == 'move':
                self.move_robot()
            elif command == 'left' or command == 'right':
                self.orientate_robot(command)
            elif command == 'report':
                self.announce_position()
            elif 'place' in command:
                self.validate_place(command.split())
            elif command == 'exit':
                break
            else:
                print('err')


PROGRAM = Robot()
PROGRAM.main()
