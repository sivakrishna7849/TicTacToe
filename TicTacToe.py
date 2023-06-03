import random
import os

logo = '''
        88                                                              
  ,d    ""              ,d                            ,d                
  88                    88                            88                
MM88MMM 88  ,adPPYba, MM88MMM ,adPPYYba,  ,adPPYba, MM88MMM ,adPPYba,  ,adPPYba,
  88    88 a8"     ""   88    ""     `Y8 a8"     ""   88   a8"     "8a a8P_____88 
  88    88 8b           88    ,adPPPPP88 8b           88   8b       d8 8PP"""""""  
  88,   88 "8a,   ,aa   88,   88,    ,88 "8a,   ,aa   88,  "8a,   ,a8" "8b,   ,aa 
  "Y888 88  `"Ybbd8"'   "Y888 `"8bbdP"Y8  `"Ybbd8"'   "Y888 `"YbbdP"'  `"Ybbd8"' 

  '''

print(logo)
interest=input("Do you want to play TicTacToe enter 'y' for yes or 'n' for no.")
skr=True
if(interest=='y'):
        skr=True
elif(interest=='n'):
        skr=False
else:
        print("wrong opinion entered.")
        skr=False

while skr is True:
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
    currentPlayer = "X"
    winner = None
    gameRunning = True

    # game board
    def printBoard(board):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])


    # take player input
    def playerInput(board):
        inp = int(input("Select a spot 1-9: "))
        if board[inp-1] == "-":
            board[inp-1] = currentPlayer
        else:
            print("Oops player is already at that spot.")


    # check for win or tie
    def checkHorizontle(board):
        global winner
        if board[0] == board[1] == board[2] and board[0] != "-":
            winner = board[0]
            return True
        elif board[3] == board[4] == board[5] and board[3] != "-":
            winner = board[3]
            return True
        elif board[6] == board[7] == board[8] and board[6] != "-":
            winner = board[6]
            return True

    def checkRow(board):
        global winner
        if board[0] == board[3] == board[6] and board[0] != "-":
            winner = board[0]
            return True
        elif board[1] == board[4] == board[7] and board[1] != "-":
            winner = board[1]
            return True
        elif board[2] == board[5] == board[8] and board[2] != "-":
            winner = board[3]
            return True


    def checkDiag(board):
        global winner
        if board[0] == board[4] == board[8] and board[0] != "-":
            winner = board[0]
            return True
        elif board[2] == board[4] == board[6] and board[4] != "-":
            winner = board[2]
            return True


    def checkIfWin(board):
        global gameRunning
        if checkHorizontle(board):
            printBoard(board)
            print(f"The winner is {winner}!")
            gameRunning = False

        elif checkRow(board):
            printBoard(board)
            print(f"The winner is {winner}!")
            gameRunning = False

        elif checkDiag(board):
            printBoard(board)
            print(f"The winner is {winner}!")
            gameRunning = False


    def checkIfTie(board):
        global gameRunning
        if "-" not in board:
            printBoard(board)
            print("It is a tie!")
            gameRunning = False


    # switch player
    def switchPlayer():
        global currentPlayer
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"


    def computer(board):
        while currentPlayer == "O":
            position = random.randint(0, 8)
            if board[position] == "-":
                board[position] = "O"
                switchPlayer()


    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        checkIfTie(board)
        switchPlayer()
        computer(board)
        checkIfWin(board)
        checkIfTie(board)
    interest=input("Do you want to play again enter 'y' for yes or 'n' for no.")
    if(interest=='y'):
        skr=True
        os.system('cls')
        print(art.logo)
    elif(interest=='n'):
        skr=False
    else:
        print("wrong opinion entered please try again.")
        skr=False
print("Thank you for Playing TicTacToe")