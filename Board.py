import numpy as np
from ChessPiece import Queen
from ChessPiece import Knight
from ChessPiece import Rook
from ChessPiece import King
from ChessPiece import Bishop
from ChessPiece import Pawn

class Board:
    
    board = np.full([8,8],'0',dtype = object)
    Rook1 = Rook(0,0,'w', "R",board)
    Rook2 = Rook(0,7,'w', "R",board)
    Knight1 = Knight(0,1,'w', "N",board)
    Knight2 = Knight(0,6,'w', "N",board)
    Bishop1 = Bishop(0,2,'w', "B",board)
    Bishop2 = Bishop(0,5,'w', "B",board)
    Kingz = King(7,4,'z', "K",board)
    Queenz = Queen(7,3,'z', "Q",board)
    King = King(0,3,'w', "K",board)
    Queen = Queen(0,4,'w', "Q",board)
    
   
   
    Pawnn=[]
    for y in range(8):
        Pawnn.append(Pawn(1,y,'w',"P",board))

    Rookz1 = Rook(7,0,'z', "R",board)
    Rookz2 = Rook(7,7,'z', "R",board)
    Knightz1 = Knight(7,1,'z', "N",board)
    Knightz2 = Knight(7,6,'z', "N",board)
    Bishopz1 = Bishop(7,2,'z', "B",board)
    Bishopz2 = Bishop(7,5,'z', "B",board)
    

    Pawnz=[]
    for x in range(8):
        Pawnz.append(Pawn(6,x,'z',"P",board))
    print(board)
   