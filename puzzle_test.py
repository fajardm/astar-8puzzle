from puzzle import Puzzle, get_none_index, neighbors, get_best_fvalue, is_goal
import unittest


class TestPuzzleClass(unittest.TestCase):

    def test_init(self):
        b = [[2, 4, 8], [5, None, 6], [7, 1, 2]]
        p = Puzzle([[2, 4, 8], [5, None, 6], [7, 1, 2]], None)
        self.assertEqual(b, p.board)
        self.assertEqual(None, p.parent)
        self.assertEqual(0, p.f)
        self.assertEqual(0, p.h)
        self.assertEqual(0, p.g)

    def test_get_none_index(self):
        b = [[2, 4, 8], [5, None, 6], [7, 1, 2]]
        i, j = get_none_index(b)
        self.assertEqual(1, i)
        self.assertEqual(1, j)

    def test_neighbors(self):
        b = [[2, 4, 8], [5, None, 6], [7, 1, 2]]
        p = neighbors(b)
        self.assertEqual(len(p), 4)
        self.assertEqual([[2, None, 8], [5, 4, 6], [7, 1, 2]], p[0].board)
        self.assertEqual([[2, 4, 8], [5, 1, 6], [7, None, 2]], p[1].board)
        self.assertEqual([[2, 4, 8], [None, 5, 6], [7, 1, 2]], p[2].board)
        self.assertEqual([[2, 4, 8], [5, 6, None], [7, 1, 2]], p[3].board)

    def test_get_best_fvalue(self):
        p1 = Puzzle([[2, 4, 8], [5, None, 6], [7, 1, 2]], None)
        p1.f = 4
        p2 = Puzzle([[2, 4, 8], [5, None, 6], [7, 1, 2]], None)
        p2.f = 8
        p3 = Puzzle([[2, 4, 8], [5, None, 6], [7, 1, 2]], None)
        p3.f = 3
        open_list = [p1, p2, p3]
        index, puzzle = get_best_fvalue(open_list)
        self.assertEqual(2, index)
        self.assertEqual(p3, puzzle)

    def test_is_goal(self):
        b = [[2, 4, 8], [5, None, 6], [7, 1, 2]]
        g1 = [[2, 4, 8], [5, None, 6], [7, 1, 2]]
        g2 = [[2, 4, 8], [5, 6, None], [7, 1, 2]]
        self.assertEqual(True, is_goal(b, g1))
        self.assertEqual(False, is_goal(b, g2))


if __name__ == '__main__':
    unittest.main()
