from Board import Board as board
class Moves:
    def RookMove(self):
        Rookplay = board.Rook1 
        pos_x = Rookplay.position_x 
        pos_y = Rookplay.position_y 
        possibleMoves = []
        bezet = False
        stukken = ''
       

        for y in  range(7):
            if board.board[pos_x][pos_y+(y+1)] == '0':
                bezet = False
                possibleMoves.append([pos_x ,pos_y+(y+1)])
                # print(possibleMoves) 
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
