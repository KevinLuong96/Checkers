import string

class CheckerBoard(object):
    # Creates the board array and populates it with checker piece objects

    def __init__(self ):
        #create and label the board
        self.xPieces = self.oPieces = 12
        self.board = []
        self.endPos = ''
        self.firstTurn = True

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

    def move(self,position, turn):
        """example: A0B1 moves the piece located at A0 to B1"""
        #defines a function to move the o or O piece to the location
        if position == "PASS":
            return True

        startX = int(string.uppercase.index(position[0])) + 1 
        startY = int(position[1])
        endX = int(string.uppercase.index(position[2])) + 1
        endY = int(position[3])
        #move piece from initial to final location
        if self.firstTurn == False:
            if abs(endX-startX) !=2 or abs(endY-startY) != 2:
                print("You must eat another piece or pass")
                return False

            if position[0:2] != self.endPos:
                print("You must move the same piece or pass")
                return False



        if turn == 'x' and self.board[startX][startY] in ['o','O']:
            print "Player 1 can only move x pieces"
            return False

        elif turn == 'o' and self.board[startX][startY] in ['x','X']:
            print "Player 2 can only move o pieces"
            return False

        if self.board[startX][startY] == 'x' and endY < startY:
            print "x pieces can only move in the down direction"
            return False

        elif self.board[startX][startY] == 'o' and endY > startY:
            print "o pieces can only move in the up direction"
            return False

        self.board[endX][endY] = self.board[startX][startY]
        self.board[startX][startY] = '-'

        if turn == 'x' and endY == 8:
            self.board[endX][endY] = 'X'

        elif turn == 'o' and endY == 1:
            self.board[endX][endY] = 'O'

        if abs(endX-startX) == 2:
            self.eat(position)
            if self.oPieces == True or self.xPieces == False:
                return True

            self.printBoard()
            print("Enter a new piece to eat or type PASS")
            return False

        #if move is called on a space two units away and there is an x in the 
        #closer space, call eat function on x 
        return True

    def eat(self,position):
        #defines an eat function for when the adjacent diagonal has an enemy
        #moves piece to new position and deletes enemy piece
        #create eat more boolean to determine if eat can be called again or pass
        startX = int(string.uppercase.index(position[0])) + 1 
        startY = int(position[1])
        endX = int(string.uppercase.index(position[2])) + 1
        endY = int(position[3])

        if self.board[endX][endY] in ['x','X']:
            self.oPieces-=1


        else:
            self.xPieces-=1

        self.board[(startX+endX)/2][(startY+endY)/2]= '-'
        self.endPos = position[2:4]
        self.firstTurn = False

        return

    def printBoard(self):
        #print every element in the area with a break between rows for player A
        for y in range(9):
            for x in range(9):
                print self.board[x][y],
            print("")


    def checkInitial(self, position):
        #determine if the input piece is legitimate
        # if string.uppercase.index(position[0])

        if position == "PASS":
            return True

        if position[0] not in string.uppercase[0:8] or\
        position[1] not in ['1','2','3','4','5','6','7','8']:
            print ("Initial space must be within the board ")
            return False

        startX = int(string.uppercase.index(position[0]) + 1)
        startY = int(position[1])

        if(self.board[startX][startY]) not in ['x','X','o','O']:
            print("The initial space is not a piece")
            return False

        return True

    def turnStart(self):
        if self.firstTurn == False:
            self.firstTurn = True

        return 

    def checkFinal(self, position):
        #determine if the final position is legitimate

        if position == "PASS":
            return True

        if position[2] not in string.uppercase[0:8] or position[3] < 1 or\
        position[3] not in ['1','2','3','4','5','6','7','8']:  
            print("Ending space must be within the board")
            return False

        startX = int(string.uppercase.index(position[0]) + 1)
        startY = int(position[1])
        endX = int(string.uppercase.index(position[2]) + 1)
        endY = int(position[3])

        #--- redundant code, if input is properly determined, players will not
        #--- be able to try to move pieces outside of board
        # if self.board[endX][endY] != '-' and 'x' and 'o' and 'X' and 'O':
        # # or \
        #     print("The ending space is off of the board")
        #     print(self.board[endX][endY])
        #     print(self.board[startX][startY])
        #     return False


        if self.board[endX][endY] == self.board[startX][startY]:
            print("There is a piece on that space") 
            return False

        elif abs(endX-startX) not in [1,2] or abs(endY-startY) not in [1,2] or\
        abs(endX-startX) != abs(endY-startY):
            print("The move must be 1x1 or 2x2 spaces away")
            return False

        elif self.board[endX][endY] != '-':
            print("The is a destination is full")
            return False

        if abs(endX-startX) == 2:
            if self.board[startX][startY] in ['x','X']:
                if self.board[(startX+endX)/2][(startY+endY)/2] in ['x','X','-']:
                    print "You can only move two spaces by eating an enemy piece"
                    return False

            elif self.board[(startX+endX)/2][(startY+endY)/2] in ['o','O','-']:
                print "You can only move two spaces by eating an enemy piece"
                return False

        return True

    def checkMove(self, position):

        if position == "HELP":
            self.help()
            return False

        if len(position) != 4:
            print ("The input must be 4 characters long")
            return False

        if self.checkInitial(position) == False:
            return False

        elif self.checkFinal(position) == False:
            return False

        else:
            return True

    def checkWin(self):
        #return true if there are no more pieces for one player
        if self.xPieces == 0:
            print("--------------------Player 2 wins!--------------------")
            return True

        elif self.oPieces == 0:
            print("--------------------Player 1 wins!--------------------")
            return True
        
        return False

        # ----------------------REMOVE WHEN DONE TESTING------------------------
        # return 

    def help(self):
        print("The objective of checkers is to remove (or eat) all of the "
            "enemy pieces" '\n'
            "Checker pieces can only move diagonally, \n and can jump spaces by "
            "eating an enemy piece." '\n'
            "Checker pieces cannot jump allied pieces. "'\n'
            "Checker pieces are allowed to eat multiple enemy pieces " 
            "in one turn,  \n but only if it is legal." '\n'
            "You cannot switch pieces after eating a piece in one turn."'\n'
            "You are not allowed to move normally after eating a piece," '\n' 
            " you must either eat another piece or pass"'\n'
            "Input moves as A3B4 where A3 is the position of the first piece \n" 
            " and B4 is the destination." '\n'
            "When eating enemy pieces, the move should be 2x2 away (A3C5) \n"
            "Checker pieces can only move in one direction, \n"
            " unless they reach the opposite side where they become King pieces \n"
            " these pieces (capital O or X) can move forwards or back")

        print("This game was created by Kevin Luong")




def main():
    """ Initialize the game and run the main loop"""
    game= CheckerBoard()
    print "--------------------------------------------------"
    print "--------------------------------------------------"
    print "--------------------------------------------------"
    print "--------------------GAME START--------------------"
    print "--------------------------------------------------"
    print "--------------------------------------------------"
    print "--------------------------------------------------"

    game.printBoard()
    print "Player 1's turn (move x pieces)"

    player1Turn = True

    while game.checkWin() == False:

        #allow player one to move O pieces and track numbers
        playerMove = raw_input("Input a place to move your piece (A2B3) or"
            " type HELP: ")

        validMove = False

        # while validMove == False:
        #     if len(playerMove) !=4:
        #         print("Input must be four characters long")
        #         playerMove = raw_input("Input a place to move your piece (A2B3):")

        #     if game.checkInitial(playerMove) == False or\
        #     game.checkFinal(playerMove) == False:
        #         playerMove = raw_input("Input a place to move your piece (A2B3):")

        #     else:
        #         validMove = True

        if player1Turn == True:
            game.turnStart()
            while game.checkMove(playerMove) == False:
                playerMove = raw_input("Input a place to move your piece"
                "(A2B3) or type HELP: ")

            while game.move(playerMove,'x') == False:
                playerMove = raw_input("Input a place to move your piece"
                "(A2B3) or type HELP: ")
                while game.checkMove(playerMove) == False:
                    playerMove = raw_input("Input a place to move your piece"
                    "(A2B3) or type HELP: ")
            print "Player 2's turn (move o pieces)"
            player1Turn = False

        else:
            game.turnStart()
            while game.checkMove(playerMove) == False:
                playerMove = raw_input("Input a place to move your piece (A2B3)"
                    "or type HELP: ")

            while game.move(playerMove,'o') == False:
                playerMove = raw_input("Input a place to move your piece"
                "(A2B3) or type HELP: ")
                while game.checkMove(playerMove) == False:
                    playerMove = raw_input("Input a place to move your piece"
                    "(A2B3) or type HELP: ")

            print "Player 1's turn (move x pieces)"
            player1Turn = True

        game.printBoard()

    return


main()





