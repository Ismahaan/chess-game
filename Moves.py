from Board import Board as board
from ChessPiece import Queen
from ChessPiece import Knight
from ChessPiece import Rook
from ChessPiece import King
from ChessPiece import Bishop
from ChessPiece import Pawn

class Moves:
    def RookMove(self):
        Rookplay = board.Rook1 
        pos_x = Rookplay.position_x 
        pos_y = Rookplay.position_y 
        possibleMoves = []

        for x in  range(7):
            if board.board[pos_x + (x+1)][pos_y] == '0':
                possibleMoves.append([pos_x+(x+1) ,pos_y])
            elif board.board2[pos_x + (x+1)][pos_y].color != Rookplay.color:
                possibleMoves.append([pos_x+(x+1) ,pos_y])
                break
            else:
                break
        return possibleMoves
    
#verzonnen door Ismahaan!!!!!
iets = Moves()
print (iets.RookMove())
    #     for x in  range(8):
    #        board.board[x][pos_y]
    #    do while (collision_horizontal == false):
            
    #        pass

    #     do while (collision_verticale ==false):

    #         pass
