import string

class CheckerBoard(object):
    # Creates the board array and populates it with checker piece objects

    def __init__(self ):
        #create and label the board
        self.xPieces = self.oPieces = 12
        self.isKing = False
        self.board = []


        for x in range(9):
            self.board.append([])

        for row in self.board:
            for i in range(9):
                row.append('-')

        #label the x axis with capital letters from A through H
        for x in range (1,9):
            self.board[x][0] = string.uppercase[x-1]

        #label the y axis with numbers from 1 through 8
        a = 1;
        for y in range (1,9):
            self.board[0][y] = a
            a+=1

        for x in range(1,9,2):
            self.board[x+1][1] = 'x'
            self.board[x][2] = 'x'
            self.board[x+1][3] = 'x'

        for x in range(1,9,2):
            self.board[x][6] = 'o'
            self.board[x+1][7] = 'o'
            self.board[x][8] = 'o'

        #pieces1 = pieces2 = 12
        #moved functionality to main

    def moveO(self,position):
        """example: A0B1 moves the piece located at A0 to B1"""
        #defines a function to move the o or O piece to the location

            #loop until a valid entry is entered
            #print("Enter a valid position: ex. A0B1")
        #if true:
            #if there is a piece in the adjacent diagonals

        #elif true:
            #if allied piece, reinput 

        #elif true:
            #if adjacent diagonals have eatable enemies call eat command
        #   eat(position)
  
        #   move(newPos)
            #call the move command again to see if any more pieces can be eaten

        #elif true:
            #input King functionality, allowing it to move backwards

            #change initial position back to -, new position to o or x, delete 
            #eaten pieces


            #pass turn
        #if move is called on a space two units away and there is an x in the 
        #closer space, call eat function on x 
        pass

    def eat(self,position):
         #defines an eat function for when the adjacent diagonal has an enemy
        #moves piece to new position and deletes enemy piece
        #create eat more boolean to determine if eat can be called again or pass
        pass

    def printBoard(self):
        #print every element in the area with a break between rows for player A
        for y in range(9):
            for x in range(9):
                print self.board[x][y],
            print("")


    def checkInitial(self, position):
        #determine if the input piece is legitimate
        # if string.uppercase.index(position[0])

        if position[0] not in string.uppercase[0:8] or\
         int(position[1]) < 1 or int(position[1]) > 8:
            print ("Initial space must be within the board ")
            return False

        startX = int(string.uppercase.index(position[0]) + 1)
        startY = int(position[1])

        if(self.board[startX][startY]) != ('x' or 'o' or 'X' or 'O'):
            print("The initial space is not a piece")
            return False

        return True

    def checkFinal(self, position):
        #determine if the final position is legitimate
        startX = int(string.uppercase.index(position[0]) + 1)
        startY = int(position[1])
        endX = int(string.uppercase.index(position[2]) + 1)
        endY = int(position[3])

        if position[2] not in string.uppercase[0:8] or position[3] < 1 or\
        int(position[3]) < 1or int(position[3]) > 8:
            print("Ending space must be within the board")
            return False

        #--------------------------TO DO ----------
        #Determine if the final position is legal

        #--- redundant code, if input is properly determined, players will not
        #--- be able to try to move pieces outside of board
        # if self.board[endX][endY] != '-' and 'x' and 'o' and 'X' and 'O':
        # # or \
        #     print("The ending space is off of the board")
        #     print(self.board[endX][endY])
        #     print(self.board[startX][startY])
        #     return False


        elif self.board[endX][endY] == self.board[startX][startY]:
            print("There is an allied piece on that space") 
            return False

        elif abs(endX-startX) not in [1,2] or abs(endY-startY) not in [1,2] or\
        abs(endX-startX) != abs(endY-startY):
            print("The move is must be 1x1 or 2x2 spaces away")
            return False

        elif self.board[endX][endY] != '-':
            print("There is a destination is full")
            return False

        elif self.board[startX][startY] in ['x','X']:
            if self.board[(startX+endX)/2][(startY+endY)/2] in ['x','X','-']:
                print "You can only move two spaces by eating an enemy piece"
                return False

        elif self.board[(startX+endX)/2][(startY+endY)/2] in ['y','Y','-']:
            print "You can only move two spaces by eating an enemy piece"
            return False

        return True


    def checkWin(self):
        #return true if there are no more pieces for one player
        if self.xPieces == 0:
        #     print("Player 2 wins!")
             return True

        elif self.oPieces == 0:
        #     print("Player 1 wins!")
            return True
        
        return False

        # ----------------------REMOVE WHEN DONE TESTING------------------------
        # return 

#   ----------------------------REMOVE WHEN DONE TESTING ------------
    def finishGame(self):
        self.xPieces = 0


def main():
    """ Initialize the game and run the main loop"""
    game= CheckerBoard()
    game.printBoard()

    player1Turn = True

    while game.checkWin() == False:

        if player1Turn == True:
            #allow player one to move O pieces and track numbers
            player1Move = raw_input("Input a place to move your piece (A2B3)")
            while len(player1Move) !=4:
                print("Input must be four characters long")
                player1Move = raw_input("Input a place to move your piece (A@B3)")

            while game.checkInitial(player1Move) == False or\
            game.checkFinal(player1Move) == False:
                player1Move = raw_input("Input a place to move your piece (A2B3)")

            game.moveO(player1Move)

            player1Turn == False
        #continue running the game loop until someone has won the game
        else:
            player1Turn == True


        #implement the turn system, player 1 can only move pieces o or O
        #player 2 can only move pieces x or X
        game.printBoard()



    return


main()


#class Piece(object):
  #defines a piece in checkers a move function

  #def __init__(self, position, isKing):
    #defines the position variable to be stored and an isKing boolean
  #  self.position = position
  #  self.isKing = False

  #def eat(location):
    #defines a function to allow checker pieces to eat others

  #def move(location):
    #defines a move function for the checker piece

  #  if(isKing==true):
      #allows a king piece to move backwards and forwards

  #  if(location != -)
      #call the eat function if the position is full






