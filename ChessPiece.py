from abc import ABCMeta, abstractmethod

class ChessPiece(metaclass=ABCMeta):
    
    @abstractmethod
    
    def __init__(self,x,y,color,symbol,board):
        self.position_x = x
        self.position_y = y
        self.color = color
        self.symbol = symbol
        board[self.position_x][self.position_y] = self.symbol
   
class Rook(ChessPiece):
    def __init__(self,x,y,color,symbol,board):
        ChessPiece.__init__(self,x,y,color,symbol,board)
        self.count = 0
        # board2[self.position_x][self.position_y] = self

class King(ChessPiece):
    def __init__(self,x,y,color,symbol,board):
        ChessPiece.__init__(self,x,y,color,symbol,board)
        self.count = 0

class Bishop(ChessPiece):
    def __init__(self,x,y,color,symbol,board):
        ChessPiece.__init__(self,x,y,color,symbol,board)

class Knight(ChessPiece):
    def __init__(self,x,y,color,symbol,board):
        ChessPiece.__init__(self,x,y,color,symbol,board)

class Pawn(ChessPiece):
    def __init__(self,x,y,color,symbol,board):
        ChessPiece.__init__(self,x,y,color,symbol,board)
        self.count = 0
#
class Queen(ChessPiece):
    def __init__(self,x,y,color,symbol,board):
        ChessPiece.__init__(self,x,y,color,symbol,board)