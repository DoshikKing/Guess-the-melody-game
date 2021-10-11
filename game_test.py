import unittest
import game

class TestGame(unittest.TestCase):
    def test_menu_a(self):
        result = game.menu(1)
        self.assertEqual(result, 0)
    
    def test_menu_b(self):
        result = game.menu(2)
        self.assertEqual(result, 1)
