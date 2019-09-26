from abc import ABCMeta, abstractmethod
import Board
class ChessPiece(metaclass=ABCMeta):
    position = 0
    
    @abstractmethod
    
    def _init_(self,x,y,color):
        self.position_x = x
        self.position_y = y
        self.color = color
   
class Rook(ChessPiece):
    def _init_(self,x,y,color,board):
        ChessPiece._init_(self,x,y,color)
        self.symbol = "R"
        board[self.position_x][self.position_y] = self


    

