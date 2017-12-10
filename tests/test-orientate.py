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
        self.current_position = []

    def test_orientate_command(self):
        """Test we can orientate the robot"""
        self.assertListEqual(orientate_robot(self.direction, self.current_position), ['0', '0', 'west'])
