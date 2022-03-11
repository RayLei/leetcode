import numpy as np
from itertools import product
from collections import defaultdict

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    board = np.array(board)

    def validate(arr):
        elem = [str(i) for i in range(1, 10)]
        res = {}
        for e in arr:
            if e == ".":
                continue
            elif e in elem and e not in res:
                res[e] = 1
            else:
                return False
        return True

    valid = True
    for row in board:
        valid = validate(row)
        if not valid:
            return False

    for i in range(9):
        valid = validate(board[:, i])
        if not valid:
            return False

    for i, j in product(range(0, 9, 3), range(0, 9, 3)):
        valid = validate(board[i: i + 3, j: j + 3].flatten())
        if not valid:
            return False

    return True


board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]



# from neetcode
def isValidSudoku_neetcode(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for r, c in product(range(9), range(9)):
        if board[r, c] == '.':
            continue
        if (board[r, c] in rows[r] or
            board[r, c] in cols[c] or
            board[r, c] in squares[r//3, c//3]):
            return False
        rows[r].add(board[r, c])
        cols[c].add(board[r, c])
        squares[r//3, c//3].add(board[r, c])

    return True

