import numpy as np
from ChessPiece import Queen
from ChessPiece import Knight
from ChessPiece import Rook
from ChessPiece import King
from ChessPiece import Bishop
from ChessPiece import Pawn

class Board:
    
    board = np.full([8,8],'0',dtype = str)
    board2 = np.full([8,8],'0',dtype = object)
    Rook1 = Rook(7,0,'w', "R",board,board2)
    Rook2 = Rook(7,7,'w', "R",board,board2)
    Knight1 = Knight(7,1,'w', "N",board,board2)
    Knight2 = Knight(7,6,'w', "N",board,board2)
    Bishop1 = Bishop(7,2,'w', "B",board,board2)
    Bishop2 = Bishop(7,5,'w', "B",board,board2)
    Kingz = King(0,4,'z', "K",board,board2)
    Queenz = Queen(4,4,'z', "Q",board,board2)
    King = King(7,3,'w', "K",board,board2)
    Queen = Queen(7,4,'w', "Q",board,board2)
    
    Pawnn=[]
    for y in range(8):
        Pawnn.append(Pawn(6,y,'w',"P",board,board2))

    Rookz1 = Rook(0,0,'z', "R",board,board2)
    Rookz2 = Rook(0,7,'z', "R",board,board2)
    Knightz1 = Knight(0,1,'z', "N",board,board2)
    Knightz2 = Knight(0,6,'z', "N",board,board2)
    Bishopz1 = Bishop(0,2,'z', "B",board,board2)
    Bishopz2 = Bishop(0,5,'z', "B",board,board2)
    

    Pawnz=[]
    for x in range(8):
        Pawnz.append(Pawn(1,x,'z',"0",board,board2))
    print(board)
   