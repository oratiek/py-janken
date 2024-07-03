import unittest

from main import judge

class TestJanken(unittest.TestCase):
    def test_draws(self):
        hands = [0, 1, 2]
        for hand in hands:
            res = judge(hand, hand)
            self.assertEqual(res, "draw")

    def test_wins(self):
        usr_hands = [0,1,2]
        ene_hands = [1,2,0]
        for i in range(3):
            res = judge(ene_hands[i], usr_hands[i])
            self.assertEqual(res, "win")

    def test_lose(self):
        usr_hands = [0,1,2]
        ene_hands = [2,0,1]
        for i in range(3):
            res = judge(ene_hands[i], usr_hands[i])
            self.assertEqual(res, "lose")

if __name__ == "__main__":
    unittest.main()
