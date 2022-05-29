import unittest
from game import Game


class GameTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test_all_one_game(self):
        for shot in range(21):
            self.game.shot(1)
        self.assertEqual(20, self.game.score())

    def test_one_strike(self):
        self.game.shot(10)
        for shot in range(2):
            self.game.shot(3)
        for shot in range(16):
            self.game.shot(0)
        self.assertEqual(22, self.game.score())

    def test_ten_strikes(self):
        self.game.shot_many(10, 10)
        self.assertEquals(300, self.game.score())

    def test_eleven_strikes(self):
        self.game.shot_many(11, 10)
        self.assertEquals(300, self.game.score())

    def test_all_strikes(self):
        self.game.shot_many(12, 10)
        self.assertEqual(300, self.game.score())


if __name__ == '__main__':
    unittest.main()
