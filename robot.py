"""
Toy Robot Simulator
Version 0.0.0
"""

class Robot(object):
    """Toy Robot Simulator"""

    def __init__(self):
        """Set base parameters"""
        self.board_bounds = range(5)
        self.position = {'x': 0, 'y': 0, 'f': 'n'}

    def announce_position(self):
        """Announce position of the robot"""
        print(str(self.position['x']) + '=x,' + str(self.position['y']) + '=y,' + self.position['f'] + '\n')

    def update_robots_position(self, pos_x=False, pos_y=False, pos_f=False):
        """Update robots position on the board"""
        if pos_x:
            self.position['x'] = pos_x

        if pos_y:
            self.position['y'] = pos_y

        if pos_f:
            self.position['f'] = pos_f

    def validate_place(self, command):
        """Validate place command"""
        if len(command) != 2:
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
        elif place[2] != 'north' and place[2] != 'south' and place[2] != 'east' and place[2] != 'west':
            print('Error with starting position F. Please enter either NORTH, SOUTH, WEST or EAST')
            return False
        else:
            self.update_robots_position(place[0], place[1], place[2])
            return True

    def move_robot(self):
        """Move the robot
            If robot is facing north or south move along the X axis
            Else move along the Y axis
        """
        move_error = False

        if self.position['f'] == 'north':
            if (int(self.position['y']) + 1) in self.board_bounds:
                self.update_robots_position(False, (int(self.position['y']) + 1), False)
            else:
                move_error = True
        elif self.position['f'] == 'south':
            if (int(self.position['y']) - 1) in self.board_bounds:
                self.update_robots_position(False, (int(self.position['y']) - 1), False)
            else:
                move_error = True

        elif self.position['f'] == 'west':
            if (int(self.position['x']) - 1) in self.board_bounds:
                self.update_robots_position((int(self.position['x']) - 1), False, False)
            else:
                move_error = True
        elif self.position['f'] == 'east':
            if (int(self.position['x']) + 1) in self.board_bounds:
                self.update_robots_position((int(self.position['x']) + 1), False, False)
            else:
                move_error = True

        return move_error

    def orientate_robot(self, direction):
        """Orientate the robot"""
        compass = ['north', 'south', 'east', 'west']
        current_position = compass.index(self.position['f'])

        if direction == 'right':
            if current_position == 0:
                self.update_robots_position(False, False, compass[2])
            elif current_position == 1:
                self.update_robots_position(False, False, compass[3])
            elif  current_position == 2:
                self.update_robots_position(False, False, compass[1])
            elif current_position == 3:
                self.update_robots_position(False, False, compass[0])
        elif direction == 'left':
            if current_position == 0:
                self.update_robots_position(False, False, compass[3])
            elif current_position == 1:
                self.update_robots_position(False, False, compass[2])
            elif  current_position == 2:
                self.update_robots_position(False, False, compass[0])
            elif current_position == 3:
                self.update_robots_position(False, False, compass[1])

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
                move = self.move_robot()
                if move:
                    print('Movement not allowed')
            elif command == 'left' or command == 'right':
                self.orientate_robot(command)
            elif command == 'report':
                self.announce_position()
            elif 'place' in command:
                self.validate_place(command.split())
            elif command == 'exit':
                break
            else:
                print('Invalid command')


PROGRAM = Robot()
PROGRAM.main()
