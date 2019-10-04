from abc import ABCMeta, abstractmethod
import numpy as np

class ChessPiece(metaclass=ABCMeta):
    
    @abstractmethod
    
    def __init__(self,x,y,color,symbol,board,board2):
        self.position_x = x
        self.position_y = y
        self.color = color
        self.symbol = symbol
        board[self.position_x][self.position_y] = self.symbol
        board2[self.position_x][self.position_y] = self
   
class Rook(ChessPiece):
    def __init__(self,x,y,color,symbol,board,board2):
        ChessPiece.__init__(self,x,y,color,symbol,board,board2)
        self.count = 0

class King(ChessPiece):
    def __init__(self,x,y,color,symbol,board,board2):
        ChessPiece.__init__(self,x,y,color,symbol,board,board2)
        self.count = 0

class Bishop(ChessPiece):
    def __init__(self,x,y,color,symbol,board,board2):
        ChessPiece.__init__(self,x,y,color,symbol,board,board2)

class Knight(ChessPiece):
    def __init__(self,x,y,color,symbol,board,board2):
        ChessPiece.__init__(self,x,y,color,symbol,board,board2)

class Pawn(ChessPiece):
    def __init__(self,x,y,color,symbol,board,board2):
        ChessPiece.__init__(self,x,y,color,symbol,board,board2)
        self.count = 0
#
class Queen(ChessPiece):
    def __init__(self,x,y,color,symbol,board,board2):
        ChessPiece.__init__(self,x,y,color,symbol,board,board2)