import string

class CheckerBoard(object):
    # Creates the board array and populates it with checker piece objects

    def __init__(self):
        self.board = []

        for x in range(9):
            self.board.append([])

        for row in self.board:
            for i in range(9):
                row.append('-');

        #for column 0 populate starting from index 1 with numbers 1 through 8
        
        for x in range (1,9):
            self.board[0][x] = string.uppercase[x-1]

        a = 1;
        for y in range (1,9):
            self.board[y][0] = a
            a+=1

        #for row 0 populate starting from index 1 with letters A through H
        #populate everything else with - 

    def moveA(self,position):
        """example: A0B1 moves the piece located at A0 to B1"""
        #defines a function to move the piece 


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


game=CheckerBoard()
game.printBoard()






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






