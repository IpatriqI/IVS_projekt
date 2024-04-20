import unittest
from mathematical_library import scitanie, odcitanie, nasobenie, delenie, eval_expr, faktorial, mocnina, odmocnina, sin, cos, tan

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
    def test_faktorial(self):
        self.assertEqual(faktorial(0), 1)
        self.assertEqual(faktorial(1), 1)
        self.assertEqual(faktorial(5), 120)
        self.assertEqual(faktorial(10), 3628800)

    def test_mocnina(self):
        self.assertEqual(mocnina(2, 3), 8)
        self.assertEqual(mocnina(3, 2), 9)
        self.assertEqual(mocnina(-2, 2), 4)
        self.assertEqual(mocnina(5, 0), 1)

    def test_odmocnina(self):
        self.assertEqual(odmocnina(8, 3), 2)
        self.assertEqual(odmocnina(16, 4), 2)
        self.assertEqual(odmocnina(9, 2), 3)

    def test_sin(self):
        self.assertAlmostEqual(sin(30), 0.5)
        self.assertAlmostEqual(sin(90), 1)
        self.assertAlmostEqual(sin(180), 0)
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(270), -1)

    def test_cos(self):
        self.assertAlmostEqual(cos(60), 0.5)
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(90), 0)
        self.assertAlmostEqual(cos(180), -1)
        
    def test_tan(self):
        self.assertAlmostEqual(tan(45), 1)
        self.assertAlmostEqual(tan(0), 0)
        self.assertAlmostEqual(tan(180), 0)
        

    def test_eval_expr(self):
        self.assertEqual(eval_expr("3 + 4 * 2"), "11")
        self.assertEqual(eval_expr("10 / 2 - 1"), "4")
        self.assertEqual(eval_expr("10 - 2 * 3"), "4")
        self.assertEqual(eval_expr("-6 - 6"), "-12")
        self.assertEqual(eval_expr("10 * (2 - 3)"), "-10")  # Test s odstranenou podporou zátvoriek zlyhá

if __name__ == '__main__':
    unittest.main()
