import unittest
from mathematical_library import scitanie, odcitanie, nasobenie, delenie, eval_expr

class TestMatematickaKniznica(unittest.TestCase):

    def test_scitanie(self):
        self.assertEqual(scitanie(1, 2), 3)
        self.assertEqual(scitanie(-1, 1), 0)
        self.assertEqual(scitanie(-1, -1), -2)

    def test_odcitanie(self):
        self.assertEqual(odcitanie(5, 3), 2)
        self.assertEqual(odcitanie(-1, 1), -2)
        self.assertEqual(odcitanie(-1, -1), 0)

    def test_nasobenie(self):
        self.assertEqual(nasobenie(3, 3), 9)
        self.assertEqual(nasobenie(-1, 1), -1)
        self.assertEqual(nasobenie(-1, -1), 1)

    def test_delenie(self):
        self.assertEqual(delenie(10, 2), 5)
        self.assertEqual(delenie(-1, 1), -1)
        self.assertEqual(delenie(5, -2), -2.5)
        with self.assertRaises(ValueError):
            delenie(1, 0)

    def test_eval_expr(self):
        self.assertEqual(eval_expr("3 + 4 * 2"), 11)
        self.assertEqual(eval_expr("10 / 2 - 1"), 4)
        self.assertEqual(eval_expr("10 - 2 * 3"), 4)
        self.assertEqual(eval_expr("10 * (2 - 3)"), -10)  # Test s odstranenou podporou zátvoriek zlyhá

if __name__ == '__main__':
    unittest.main()
