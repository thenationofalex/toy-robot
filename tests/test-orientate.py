"""
Toy Robot Simulator
Test - Orientate Robot
"""
import unittest

from modules.orientate import orientate_robot

class TestOrientateRobot(unittest.TestCase):
    """Test Orientate Robot"""

    def setUp(self):
        """Setup"""
        self.direction = 'left'
        self.current_position = {'x': '0', 'y': '0', 'f': 'south'}
        self.expected = {'x': '0', 'y': '0', 'f': 'east'}

    def test_orientate_command(self):
        """Test we can orientate the robot"""
        self.assertDictEqual(orientate_robot(self.direction, self.current_position), self.expected)
