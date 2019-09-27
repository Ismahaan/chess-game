import numpy as np
from ChessPiece import Rook

class Board:
    board = np.zeros([8,8], dtype = object)
    Rook1 = Rook(0,0,'w',board)
    # Undefined variable 'Rook'pylint(undefined-variable)
    print(board)