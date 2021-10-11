import unittest
from unittest import result
import game

class TestGame(unittest.TestCase):
    def test_menu(self):
        result = game.menu(1)
        self.assertEqual(result, 0)
        self.assertEqual(result, 1)

    def test_start_game(self):
        result = game.start_game()
        self.assertEqual(result, "Good")

    def test_get_random_song(self):
        result = game.get_random_song()
        self.assertEqual(result, "song.mp3")

    def test_get_songs(self):
        result = game.get_songs()
        self.assertEqual(result, ["song.mp3"])

    def test_get_variants(self):
        result = game.get_var()
        self.assertEqual(result, "song.mp3")