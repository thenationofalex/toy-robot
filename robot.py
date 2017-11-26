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
        print('x=' + str(self.position['x']) + ', y=' + \
              str(self.position['y']) + ', f=' + str(self.position['f']) + '\n')

    def validate_place(self, command):
        """Validate place command"""
        if len(command) != 2:
            return False

        place = command[1].split(',')

        if isinstance(place[0], int) or isinstance(place[1], int):
            if command[0] != 'place':
                print('Error please enter a valid command')
                return False
            elif int(place[0]) not in self.board_bounds:
                print('Error please enter a value between 0 & 4')
                return False
            elif int(place[1]) not in self.board_bounds:
                print('Error please enter a value between 0 & 4')
                return False
            elif place[2] != 'north' and place[2] != 'south' \
                and place[2] != 'east' and place[2] != 'west':
                print('Error with starting position F. Please enter either NORTH, SOUTH, WEST or EAST')
                return False
            else:
                self.position['x'] = place[0]
                self.position['y'] = place[1]
                self.position['f'] = place[2]
                return True
        else:
            return False

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

    def orientate_robot(self, direction):
        """Orientate the robot"""
        compass = ['north', 'south', 'east', 'west']
        current_position = compass.index(self.position['f'])

        if direction == 'right':
            if current_position == 0:
                self.position['f'] = compass[2]
            elif current_position == 1:
                self.position['f'] = compass[3]
            elif  current_position == 2:
                self.position['f'] = compass[1]
            elif current_position == 3:
                self.position['f'] = compass[0]
        elif direction == 'left':
            if current_position == 0:
                self.position['f'] = compass[3]
            elif current_position == 1:
                self.position['f'] = compass[2]
            elif  current_position == 2:
                self.position['f'] = compass[0]
            elif current_position == 3:
                self.position['f'] = compass[1]

    @classmethod
    def menu(cls):
        """Return cli menu"""
        return print('Available commands:\n- PLACE X, Y, F\n- MOVE\n- LEFT\n- RIGHT\n- REPORT\n- EXIT\n\n')

    def main(self):
        """Start robot simulator"""
        print('Toy Robot Simulator\n')
        start_command = False

        while start_command is False:
            start_command = self.validate_place(
                input('Please enter a starting position (place X,Y,F):\n\n').lower().split()
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
