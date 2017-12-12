"""
Toy Robot Simulator
Test - Move Robot
"""
import unittest

from modules.move import move_robot

class TestMovingRobot(unittest.TestCase):
    """Test moving robot"""

    def setUp(self):
        self.test_board = range(5)
        self.test_position = {'x': '1', 'y': '1', 'f': 'south'}
        self.expected =  {'x': '1', 'y': '0', 'f': 'south'}

    def test_movement(self):
        """Test we can move the robot"""
        self.assertDictEqual(move_robot(self.test_position, self.test_board), self.expected)
