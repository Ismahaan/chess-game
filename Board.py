import numpy as np
from abc import ABCMeta, abstractmethod
class Board:
    board = np.zeros([8,8], dtype = int)
    Rook1 = Rook(0,0,'w',board)
    # Undefined variable 'Rook'pylint(undefined-variable)
    print(board)
    
        
