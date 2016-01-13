import string

class CheckerBoard(object):
    # Creates the board array and populates it with checker piece objects

    def __init__(self, ):
        #create and label the board
        self.board = []

        for x in range(9):
            self.board.append([])

        for row in self.board:
            for i in range(9):
                row.append('-');

        #label the x axis with capital letters from A through H
        for x in range (1,9):
            self.board[0][x] = string.uppercase[x-1]

        #label the y axis with numbers from 1 through 8
        a = 1;
        for y in range (1,9):
            self.board[y][0] = a
            a+=1

        for x in range(1,9,2):
            self.board[1][x] = 'x'
            self.board[2][x+1] = 'x'
            self.board[3][x] = 'x'

        for x in range(1,9,2):
            self.board[6][x] = 'o'
            self.board[7][x+1] = 'o'
            self.board[8][x] = 'o'

        pieces1 = pieces2 = 12

    def moveA(self,position, piece):
        """example: A0B1 moves the piece located at A0 to B1"""
        #defines a function to move the piece to the location
        #piece allows one player to only control one type of piece


        #while position.length != 4:
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

            #change initial position back to -, new position to o or x, delete eaten 
            #pieces


            #pass turn
        pass

    def eat(self,position):
         #defines an eat function for when the adjacent diagonal has an enemy
        #moves piece to new position and deletes enemy piece
        pass

    def printBoard(self):
        #print every element in the area with a break between rows for player A
        for x in range(9):
            for y in range(9):
                print self.board[x][y],
            print("")

    def printBoardB(self):
        #print every element in the area with a break between rows for player B
        pass

    def checkWin(self):
        #return true if there are no more pieces for one player
        if pieces1 == 0:
            print("Player 2 wins!")
            return True

        elif pieces2 == 0:
            print("Player 1 wins!")
            return True
        #else return false

        return False


def main():
    """ Initialize the game and run the main loop"""
    game= CheckerBoard()
    game.printBoard()

    while(checkWin == False):
        #continue running the game loop until someone has won the game

        #implement the turn system, player 1 can only move pieces o or O
        #player 2 can only move pieces x or X
    return


main()



#class Piece(object):
  #defines a piece in checkers a move function

  #def __init__(self, position, isKing):
    #defines the position variable to be stored and an isKing boolean
  #  self.position = position
  #  self.isKing = false

  #def eat(location):
    #defines a function to allow checker pieces to eat others

  #def move(location):
    #defines a move function for the checker piece

  #  if(isKing==true):
      #allows a king piece to move backwards and forwards

  #  if(location != -)
      #call the eat function if the position is full






