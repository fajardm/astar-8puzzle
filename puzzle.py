# functional programming
from copy import deepcopy


class Puzzle:
    def __init__(self, start, parent):
        self.board = start
        self.parent = parent
        self.f = 0  # hasil fungsi a star
        self.g = 0  # jumlah angka yg salah
        self.h = 0  # manhattan distance


def generate():
    board = [[3, 4, 8], [5, None, 6], [7, 1, 2]]
    return board


def get_none_index(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                return i, j


def neighbors(puzzle):
    board = puzzle.board
    list_of_neighbors = []
    x, y = get_none_index(board)
    if x > 0:
        new_board = deepcopy(board)
        new_board[x][y] = new_board[x - 1][y]
        new_board[x - 1][y] = None
        successor = Puzzle(new_board, puzzle)
        list_of_neighbors.append(successor)
    if x < 2:
        new_board = deepcopy(board)
        new_board[x][y] = new_board[x + 1][y]
        new_board[x + 1][y] = None
        successor = Puzzle(new_board, puzzle)
        list_of_neighbors.append(successor)
    if y > 0:
        new_board = deepcopy(board)
        new_board[x][y] = new_board[x][y - 1]
        new_board[x][y - 1] = None
        successor = Puzzle(new_board, puzzle)
        list_of_neighbors.append(successor)
    if y < 2:
        new_board = deepcopy(board)
        new_board[x][y] = new_board[x][y + 1]
        new_board[x][y + 1] = None
        successor = Puzzle(new_board, puzzle)
        list_of_neighbors.append(successor)
    return list_of_neighbors


def get_best_fvalue(open_list):
    f = open_list[0].f
    index = 0
    for i, item in enumerate(open_list):
        if i == 0:
            continue
        if item.f < f:
            f = item.f
            index = i
    return index, open_list[index]


def is_goal(board, goal):
    return board == goal
