"""
Toy Robot Simulator
Test - Input Controller
"""
import unittest

from modules.inputcontroller import input_controller

class TestInputController(unittest.TestCase):
    """Test input controller"""

    def setUp(self):
        self.test_command = 'place 0,0,south'
        self.test_board = range(5)
        self.test_position = {'x': 1, 'y': 1, 'f': 'south'}
        self.expected = ['0','0','south']

    def test_controller(self):
        """Test we can process a command"""
        self.assertListEqual(input_controller(
            self.test_command,
            self.test_position,
            self.test_board
        ), self.expected)
