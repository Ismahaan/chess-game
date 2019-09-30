import numpy as np
from ChessPiece import Queen
from ChessPiece import Knight
from ChessPiece import Rook
from ChessPiece import King
from ChessPiece import Bishop
from ChessPiece import Pawn

class Board:
    
    board = np.full([8,8],'0',dtype = object)
    Rook1 = Rook(0,0,'w',board)
    Rook2 = Rook(0,7,'w',board)
    Knight1 = Knight(0,1,'w',board)
    Knight2 = Knight(0,6,'w',board)
    Bishop1 = Bishop(0,2,'w',board)
    Bishop2 = Bishop(0,5,'w',board)
    Kingz = King(7,4,'z',board)
    Queenz = Queen(7,3,'z',board)
    King = King(0,3,'w',board)
    Queen = Queen(0,4,'w',board)
    
   
   
    Pawnn=[]
    for y in range(8):
        Pawnn.append(Pawn(1,y,'w',board))

    Rookz1 = Rook(7,0,'z',board)
    Rookz2 = Rook(7,7,'z',board)
    Knightz1 = Knight(7,1,'z',board)
    Knightz2 = Knight(7,6,'z',board)
    Bishopz1 = Bishop(7,2,'z',board)
    Bishopz2 = Bishop(7,5,'z',board)
    

    Pawnz=[]
    for x in range(8):
        Pawnz.append(Pawn(6,x,'z',board))
    print(board)
   