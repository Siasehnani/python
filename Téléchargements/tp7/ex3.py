import unittest
import ex1tp7

class TestConversion(unittest.TestCase):

    def test_dollars_to_dirhams(self):
        self.assertEqual(ex1tp7.dollars_to_dirhams(10), 100)
        self.assertEqual(ex1tp7.dollars_to_dirhams(0), 0)
        self.assertEqual(ex1tp7.dollars_to_dirhams(1), 10)
        self.assertAlmostEqual(ex1tp7.dollars_to_dirhams(1.5), 15)

    def test_meters_to_kilometers(self):
        self.assertEqual(ex1tp7.meters_to_kilometers(1000), 1)
        self.assertEqual(ex1tp7.meters_to_kilometers(0), 0)
        self.assertEqual(ex1tp7.meters_to_kilometers(500), 0.5)
        self.assertAlmostEqual(ex1tp7.meters_to_kilometers(1500), 1.5)

if __name__ == '__main__':
    unittest.main()
