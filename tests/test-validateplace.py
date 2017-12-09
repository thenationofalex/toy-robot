"""
Toy Robot Simulator
Test - Validate Place
"""
import unittest

from modules.validateplace import validate_place

class TestValidatePlace(unittest.TestCase):

    def test_valid_place_command(self):
        """Valid command"""
        test_command = 'PLACE 0,0,NORTH'
        test_board = range(5)

        self.assertTrue(validate_place(test_command, test_board))

    def test_invalid_place_command(self):
        """Invalid command"""
        test_command = 'PLACE 5,5,FOO'
        test_board = range(5)

        self.assertFalse(validate_place(test_command, test_board))

if __name__ == '__main__':
    unittest.main()
