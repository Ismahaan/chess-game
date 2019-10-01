from abc import ABCMeta, abstractmethod

class ChessPiece(metaclass=ABCMeta):
    
    @abstractmethod
    
    def __init__(self,x,y,color):
        self.position_x = x
        self.position_y = y
        self.color = color
   
class Rook(ChessPiece):
    def __init__(self,x,y,color,board):
        ChessPiece.__init__(self,x,y,color)
        self.symbol = "R"
        self.count = 0
        board[self.position_x][self.position_y] = self.symbol
        board2[self.position_x][self.position_y] = self

class King(ChessPiece):
    def __init__(self,x,y,color,board):
        ChessPiece.__init__(self,x,y,color)
        self.symbol = "K"
        self.count = 0
        board[self.position_x][self.position_y] = self.symbol

class Bishop(ChessPiece):
    def __init__(self,x,y,color,board):
        ChessPiece.__init__(self,x,y,color)
        self.symbol = "B"
        board[self.position_x][self.position_y] = self.symbol

class Knight(ChessPiece):
    def __init__(self,x,y,color,board):
        ChessPiece.__init__(self,x,y,color)
        self.symbol = "k"
        board[self.position_x][self.position_y] = self.symbol

class Pawn(ChessPiece):
    def __init__(self,x,y,color,board):
        ChessPiece.__init__(self,x,y,color)
        self.symbol = "0"
        self.count = 0
        board[self.position_x][self.position_y] = self.symbol
#
class Queen(ChessPiece):
    def __init__(self,x,y,color,board):
        ChessPiece.__init__(self,x,y,color)
        self.symbol = "Q"
        board[self.position_x][self.position_y] = self.symbol
