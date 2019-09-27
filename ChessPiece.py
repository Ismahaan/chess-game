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
        board[self.position_x][self.position_y] = self.symbol
