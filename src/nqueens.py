# Elliot Mayer
def nqueens(n):
    def solve(state: list[list[int]], col: int, queens: list[tuple[int, int]]):
        if len(queens) == n:
            return [q[0] for q in sorted(queens, key=lambda x: x[1])] # sort by the columns and just display row indices
        elif col >= n:
            return False

        for move in expand(state, col, queens):
            new_state = [row[:] for row in state]  # copy board
            new_state[move[0]][move[1]] = 1  # place queen
            result = solve(new_state, col + 1, queens + [move])
            if result:
                return result  # exit
        return False

    # Initialize empty board
    initial_state = [[0] * n for _ in range(n)]
    return solve(initial_state, 0, [])


def expand(state: list[list[int]], col: int, queens: list[tuple[int, int]])-> list:
    """
    :param state: board state, represented as a list of lists containing 1 for queens and 0 for empty spaces
    :param col: the col index that we want to expand
    :param queens: locations of all queens
    :return: valid_moves
    """
    n = len(state)
    valid_moves = []

    for row in range(n):
        new_location = (row, col)
        is_valid = True

        for queen in queens:
            if attacking(queen, new_location):
                is_valid = False
                break

        if is_valid:
            valid_moves.append(new_location)

    return valid_moves


def attacking(queen1: tuple, queen2: tuple )-> bool:
    if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
        return True
    if queen1[0] - queen1[1] == queen2[0] - queen2[1] or queen1[0] + queen1[1] == queen2[0] + queen2[1]:
        return True
    return False





