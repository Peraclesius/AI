def nqueens(n):
    pass





def expand(state: [list[list]], col: int, queens: list[tuple])-> list:
    """
    :param state: board state, represented as a list of lists containing 1 for queens and 0 for empty spaces
    :param col: the col index that we want to expand
    :param queens: locations of all queens
    :return: valid_moves
    """
    n = len(state)
    # movements = [-1, 1] # up, down
    # location =  (row, 0)
    # new_location = None
    valid_moves = []
    # if the selected row is all False, so initially
    # if len(set(state[row][:])) != 1:
    #     pass

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





