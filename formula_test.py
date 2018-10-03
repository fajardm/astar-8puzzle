from formula import manhattan
import unittest


class TestFormula(unittest.TestCase):

    def test_manhattan(self):
        b = [[8, 1, 3], [4, None, 2], [7, 6, 5]]
        g1 = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
        h = manhattan(b, g1)
        self.assertEqual(10, h)


if __name__ == '__main__':
    unittest.main()
