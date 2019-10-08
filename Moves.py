from Board import Board as board
from ChessPiece import Queen
from ChessPiece import Knight
from ChessPiece import Rook
from ChessPiece import King
from ChessPiece import Bishop
from ChessPiece import Pawn

class Moves:
    def RookMove(self,rook):
      
        pos_x = rook.position_x 
        pos_y = rook.position_y 
        possibleMoves = []

        for x in  range(7):
            if (pos_x + x) < 7:
                if board.board[pos_x + (x+1)][pos_y] == '0':
                    possibleMoves.append([pos_x+(x+1) ,pos_y])
                elif board.board2[pos_x + (x+1)][pos_y].color != rook.color:
                    possibleMoves.append([pos_x+(x+1) ,pos_y])
                    break
                else:
                    break
            else: 
                break
       

        for x in  range(7):
            if (pos_x - x) > 0:
                if board.board[pos_x - (x+1)][pos_y] == '0':
                    possibleMoves.append([pos_x- (x+1) ,pos_y])
                elif board.board2[pos_x - (x+1)][pos_y].color != rook.color:
                    possibleMoves.append([pos_x-(x+1) ,pos_y])
                    break
                else:
                    break
            else: 
                break
        

        for y in  range(7):
            if (pos_y + y) < 7:
                if board.board[pos_x ][pos_y+ (y+1)] == '0':
                    possibleMoves.append([pos_x ,pos_y+ (y+1)])
                elif board.board2[pos_x ][pos_y+ (y+1)].color != rook.color:
                    possibleMoves.append([pos_x ,pos_y+ (y+1)])
                    break
                else:
                    break
            else: 
                break
        

        for y in  range(7):
            if (pos_y - y) > 0:
                if board.board[pos_x ][pos_y- (y+1)] == '0':
                    possibleMoves.append([pos_x ,pos_y- (y+1)])
                elif board.board2[pos_x ][pos_y- (y+1)].color != rook.color:
                    possibleMoves.append([pos_x ,pos_y- (y+1)])
                    break
                else:
                    break
            else: 
                break
        return possibleMoves


    def BishopMove(self,bishop):
        pos_x = bishop.position_x 
        pos_y = bishop.position_y 
        possibleMoves = []

        for x in  range(7):
            if (pos_x + x) < 7 and (pos_y + x) <7:
                if board.board[pos_x + (x+1)][pos_y+ (x+1)] == '0':
                    possibleMoves.append([pos_x+(x+1) ,pos_y + (x+1)])
                elif board.board2[pos_x + (x+1)][pos_y + (x+1)].color != bishop.color:
                    possibleMoves.append([pos_x+(x+1) ,pos_y + (x+1)])
                    break
                else:
                    break
                
            else: 
                break
 

        for x in  range(7):
            if (pos_x + x) < 7 and (pos_y - x) > 0:
                if board.board[pos_x + (x+1)][pos_y- (x+1)] == '0':
                    possibleMoves.append([pos_x+(x+1) ,pos_y - (x+1)])
                elif board.board2[pos_x + (x+1)][pos_y - (x+1)].color != bishop.color:
                    possibleMoves.append([pos_x+(x+1) ,pos_y - (x+1)])
                    break
                else:
                    break
                
            else: 
                break

        for x in  range(7):
            if (pos_x - x) > 0 and (pos_y + x) <7:
                if board.board[pos_x - (x+1)][pos_y+ (x+1)] == '0':
                    possibleMoves.append([pos_x-(x+1) ,pos_y + (x+1)])
                elif board.board2[pos_x - (x+1)][pos_y + (x+1)].color != bishop.color:
                    possibleMoves.append([pos_x-(x+1) ,pos_y + (x+1)])
                    break
                else:
                    break
                
            else: 
                break
        

        for x in  range(7):
            if (pos_x - x) > 0 and (pos_y - x) >0:
                if board.board[pos_x - (x+1)][pos_y- (x+1)] == '0':
                    possibleMoves.append([pos_x-(x+1) ,pos_y - (x+1)])
                elif board.board2[pos_x - (x+1)][pos_y - (x+1)].color != bishop.color:
                    possibleMoves.append([pos_x-(x+1) ,pos_y - (x+1)])
                    break
                else:
                    break
                
            else: 
                break
        return possibleMoves

    def QueenMoves(self,queen):
        pos_x = queen.position_x 
        pos_y = queen.position_y 
        possibleMoves = []

        for x in  range(7):
            if (pos_x + x) < 7:
                if board.board[pos_x + (x+1)][pos_y] == '0':
                    possibleMoves.append([pos_x+(x+1) ,pos_y])
                elif board.board2[pos_x + (x+1)][pos_y].color != queen.color:
                    possibleMoves.append([pos_x+(x+1) ,pos_y])
                    break
                else:
                    break
            else: 
                break
       

        for x in  range(7):
            if (pos_x - x) > 0:
                if board.board[pos_x - (x+1)][pos_y] == '0':
                    possibleMoves.append([pos_x- (x+1) ,pos_y])
                elif board.board2[pos_x - (x+1)][pos_y].color != queen.color:
                    possibleMoves.append([pos_x-(x+1) ,pos_y])
                    break
                else:
                    break
            else: 
                break
        

        for y in  range(7):
            if (pos_y + y) < 7:
                if board.board[pos_x ][pos_y+ (y+1)] == '0':
                    possibleMoves.append([pos_x ,pos_y+ (y+1)])
                elif board.board2[pos_x ][pos_y+ (y+1)].color != queen.color:
                    possibleMoves.append([pos_x ,pos_y+ (y+1)])
                    break
                else:
                    break
            else: 
                break
        

        for y in  range(7):
            if (pos_y - y) > 0:
                if board.board[pos_x ][pos_y- (y+1)] == '0':
                    possibleMoves.append([pos_x ,pos_y- (y+1)])
                elif board.board2[pos_x ][pos_y- (y+1)].color != queen.color:
                    possibleMoves.append([pos_x ,pos_y- (y+1)])
                    break
                else:
                    break
            else: 
                break
        
        for x in  range(7):
            if (pos_x + x) < 7 and (pos_y + x) <7:
                if board.board[pos_x + (x+1)][pos_y+ (x+1)] == '0':
                    possibleMoves.append([pos_x+(x+1) ,pos_y + (x+1)])
                elif board.board2[pos_x + (x+1)][pos_y + (x+1)].color != queen.color:
                    possibleMoves.append([pos_x+(x+1) ,pos_y + (x+1)])
                    break
                else:
                    break
            else: 
                break
 

        for x in  range(7):
            if (pos_x + x) < 7 and (pos_y - x) > 0:
                if board.board[pos_x + (x+1)][pos_y- (x+1)] == '0':
                    possibleMoves.append([pos_x+(x+1) ,pos_y - (x+1)])
                elif board.board2[pos_x + (x+1)][pos_y - (x+1)].color != queen.color:
                    possibleMoves.append([pos_x+(x+1) ,pos_y - (x+1)])
                    break
                else:
                    break
                
            else: 
                break

        for x in  range(7):
            if (pos_x - x) > 0 and (pos_y + x) <7:
                if board.board[pos_x - (x+1)][pos_y+ (x+1)] == '0':
                    possibleMoves.append([pos_x-(x+1) ,pos_y + (x+1)])
                elif board.board2[pos_x - (x+1)][pos_y + (x+1)].color != queen.color:
                    possibleMoves.append([pos_x-(x+1) ,pos_y + (x+1)])
                    break
                else:
                    break
                
            else: 
                break
        

        for x in  range(7):
            if (pos_x - x) > 0 and (pos_y - x) >0:
                if board.board[pos_x - (x+1)][pos_y- (x+1)] == '0':
                    possibleMoves.append([pos_x-(x+1) ,pos_y - (x+1)])
                elif board.board2[pos_x - (x+1)][pos_y - (x+1)].color != queen.color:
                    possibleMoves.append([pos_x-(x+1) ,pos_y - (x+1)])
                    break
                else:
                    break
            else: 
                break
        return possibleMoves



    
#verzonnen door Ismahaan!!!!!
iets = Moves()
print (iets.QueenMoves(board.Queenz))
