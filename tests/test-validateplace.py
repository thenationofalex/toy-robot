"""
Toy Robot Simulator
Test - Validate Place
"""
import unittest

from modules.validateplace import validate_place

class TestValidatePlace(unittest.TestCase):
    """Test Validate Place"""

    def setUp(self):
        self.expected =  {'x': '0', 'y': '0', 'f': 'north'}
        self.test_board = range(5)

    def test_valid_place_command(self):
        """Valid command"""
        test_command = 'PLACE 0,0,NORTH'

        self.assertDictEqual(validate_place(test_command, self.test_board), self.expected)

    def test_invalid_place_command(self):
        """Invalid command"""
        test_command = 'PLACE 5,5,FOO'

        self.assertFalse(validate_place(test_command, self.test_board))

if __name__ == '__main__':
    unittest.main()
