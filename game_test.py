import unittest
from unittest import result
import game

class TestGame(unittest.TestCase):
    def test_menu_a(self):
        result = game.menu(1)
        self.assertEqual(result, 0)
    
    def test_menu_b(self):
        result = game.menu(2)
        self.assertEqual(result, 1)

    def test_start_game(self):
        result = game.start_game()
        self.assertEqual(result, "Good")

    def test_get_random_song(self):
        result = game.start_game()
        self.assertEqual(result, "song.mp3")