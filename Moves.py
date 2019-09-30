from Board import Board as board
class Moves:
    def RookMove(self):
        Rookplay = board.Rook1 
        pos_x = Rookplay.position_x 
        pos_y = Rookplay.position_y 
        possibleMoves = []
        bezet = False
        stukken = ''
       

        for x in  range(7):
            if board.board[pos_x + (x+1)][pos_y] == '0':
                bezet = False
                possibleMoves.append([pos_x+(x+1) ,pos_y])
            # elif board.board[pos_x + (x+1)][pos_y].color != Rook.self.color:
            #     possibleMoves.append([pos_x+(x+1) ,pos_y])
            else:
                break
        return possibleMoves
    
#verzonnen door Ismahaan!!!!!
iets = Moves()
print (iets.RookMove())
    
