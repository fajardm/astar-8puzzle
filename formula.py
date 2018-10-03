# functional programming
from puzzle import get_best_fvalue, is_goal, neighbors


def manhattan(board, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            tile = board[i][j]
            if tile is not None:
                for ig in range(3):
                    for jg in range(3):
                        if tile == goal[ig][jg]:
                            h += abs(i - ig) + abs(j - jg)
    return h


def output(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle.board[i][j] is not None:
                print(puzzle.board[i][j], end=' ')
            else:
                print(' ', end=' ')
        print("")

    print("F =", puzzle.g, "+", puzzle.h, "=", puzzle.f)
    print("")


def astar(puzzle, goal, depth):
    open_list = []
    closed_list = []
    open_list.append(puzzle)

    i = 0
    while open_list:
        if depth is not None and i >= depth:
            break

        index, current = get_best_fvalue(open_list)
        if is_goal(current.board, goal):
            print("goal")
            output(current)
            return current

        print("current")
        output(current)

        open_list.pop(index)
        closed_list.append(current)

        neighbor_list = neighbors(current)
        for neighbor in neighbor_list:
            is_closed = False
            for i, closed in enumerate(closed_list):
                if closed.board == neighbor.board:
                    is_closed = True
                    break

            if not is_closed:
                is_open = False
                tentative_gscore = current.g + 1

                for j, opened in enumerate(open_list):
                    if opened.board == neighbor.board:
                        is_open = True
                        if tentative_gscore < open_list[j].g:
                            open_list[j].g = tentative_gscore
                            open_list[j].f = open_list[j].g + open_list[j].h
                            open_list[j].parent = current
                        break

                if not is_open:
                    neighbor.g = tentative_gscore
                    neighbor.h = manhattan(neighbor.board, goal)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current
                    open_list.append(neighbor)

        i += 1

    return None
