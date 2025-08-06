import random 

spots = [1,2,3,4,5,6,7,8,9]
board = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
clmn = 3

def drawBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(clmn):
            print("", board[x][y], end=" |")
    print("\n+---+---+---+")
    


def modify(num, turn):
    num -= 1
    if(num == 0):
        board[0][0] = turn
    elif(num == 1):
        board[0][1] = turn
    elif(num == 2):
        board[0][2] = turn
    elif(num == 3):
        board[1][0] = turn
    elif(num == 4):
        board[1][1] = turn
    elif(num == 5):
        board[1][2] = turn
    elif(num == 6):
        board[2][0] = turn
    elif(num == 7):
        board[2][1] = turn
    elif(num == 8):
        board[2][2] = turn

def checkForWinner(board):
    ### X axis
    if(board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        print("O has won!")
        return "O"
    elif(board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
        print("O has won!")
        return "O"
    elif(board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
    ### Y axis
    elif(board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
        print("O has won!")
        return "O"
    elif(board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
        print("O has won!")
        return "O"
    elif(board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
    ### Cross wins
    elif(board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
    elif(board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        print("O has won!")
        return "O"
    else:
        return "Tie"

def startGame():
    leaveLoop = False
    turnCounter = 0
    print("Welcome to Tic Tac Toe!")
    print("-----------------------")
    while(leaveLoop == False):
        ### It's the player turn
        if(turnCounter % 2 == 1):
            drawBoard()
            number = int(input("\nEnter the number according to the position: "))
            if(number >= 1 and number <= 9):
                modify(number, 'X')
                spots.remove(number)
            else:
                print("Invalid input. Please try again. ")
            turnCounter += 1
        ### It's the computer's turn
        else:
            while(True):
                cpuChoice = random.choice(spots)
                print("\nCPU choice: ",cpuChoice)
                if(cpuChoice in spots):
                    modify(cpuChoice, 'O')
                    spots.remove(cpuChoice)
                    turnCounter += 1
                    break
        winner = checkForWinner(board)
        if(winner != "Tie"):
            print("\nGame over! Thank you for playing :)")
            break

startGame()