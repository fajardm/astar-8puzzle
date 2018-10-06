from formula import astar
from puzzle import Puzzle


def main():
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
    board = [[3, 4, 8], [5, None, 6], [7, 1, 2]]
    # board = [[None, 1, 3], [4, 2, 5], [7, 8, 6]] # simple board
    puzzle = Puzzle(board, None)
    depth = 100
    astar(puzzle, goal, depth)


if __name__ == "__main__":
    main()
