"""
Toy Robot Simulator
Version 0.0.0
"""

class Robot(object):
    """Toy Robot Simulator"""

    def __init__(self):
        """Set base parameters"""
        self.position = {'x': 0, 'y': 0, 'f': 'n'}
        self.board_bounds = range(1, 5)

    def announce_position(self):
        """Announce position of the robot"""
        print('🤖 ' + self.position['x'] + ',' + self.position['y'] + ',' + self.position['f'] + '\n')

    def update_robots_position(self, pos_x, pos_y, pos_f):
        """Update robots position on the board"""
        self.position['x'] = pos_x
        self.position['y'] = pos_y

        if pos_f == 'n':
            pos_f = 'NORTH'
        elif pos_f == 's':
            pos_f = 'SOUTH'
        elif pos_f == 'e':
            pos_f = 'EAST'
        elif pos_f == 'w':
            pos_f = 'WEST'
        
        self.position['f'] = pos_f
        self.announce_position()

    def validate_place(self, command):
        """Validate place command"""
        place = command[1].split(',')

        if command[0] != 'place':
            print('Error please enter a valid command')
            return False
        elif int(place[0]) not in self.board_bounds:
            print('Error please enter a value between 1 & 5')
            return False
        elif int(place[1]) not in self.board_bounds:
            print('Error please enter a value between 1 & 5')
            return False
        elif place[2] != 'n' and place[2] != 's' and place[2] != 'e' and place[2] != 'w':
            print('Error with starting position F. Please enter either N, S, W or E')
            return False
        else:
            self.update_robots_position(place[0], place[1], place[2])
            return True

    @classmethod
    def menu(cls):
        """Return cli menu"""
        return input('Available commands:\nPLACE X, Y, F\nMOVE\nLEFT\nRIGHT\nREPORT\n\n')

    def main(self):
        """Start robot simulator"""
        print('🤖 Toy Robot Simulator\n')
        start_command = False

        while start_command is False:
            start_command = input('Please enter a starting position:\n\n').lower().split()

            if len(start_command) == 2:
                start_command = self.validate_place(start_command)
            else:
                start_command = False
        
        while True:
            self.menu()


PROGRAM = Robot()
PROGRAM.main()
