def nqueens(n):
    pass



'''
same line check: X1 = X2
same column check: Y1 = Y2
same diagonal check: X1-Y1 = X2-Y2 or X1+Y1 = X2+Y2

'''

def attacking(queen1: tuple, queen2: tuple )-> bool:
    if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
        return True
    if queen1[0] - queen1[1] == queen2[0] - queen2[1] or queen1[0] + queen1[1] == queen2[0] + queen2[1]:
        return True
    return False





