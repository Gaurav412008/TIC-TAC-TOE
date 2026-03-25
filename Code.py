# TIC TAC TOE :)

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

CurrentPlayer = "X"
winner = None
gameRunning = True

# Print board

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player input

def playerinput(board):
    try:
        inp = int(input(f"Player {CurrentPlayer}, enter 1-9: "))
        if 1 <= inp <= 9 and board[inp-1] == "-":
            board[inp-1] = CurrentPlayer
        else:
            print("Invalid move!")
            playerinput(board)
    except:
        print("Please enter a number!")
        playerinput(board)

# Win check1

def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True
    return False

def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True
    return False

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True
    return False

def checktie(board):
    global gameRunning
    if "-" not in board and winner is None:
        printboard(board)
        print("It's a tie!")
        gameRunning = False

def checkwin():
    global gameRunning
    if checkhorizontal(board) or checkrow(board) or checkdiagonal(board):
        printboard(board)
        print(f"The winner is {winner}!!!!")
        gameRunning = False

# Safe winner check for minimax

def check_winner_temp(board):
    if board[0] == board[1] == board[2] != "-":
        return board[0]
    if board[3] == board[4] == board[5] != "-":
        return board[3]
    if board[6] == board[7] == board[8] != "-":
        return board[6]

    if board[0] == board[3] == board[6] != "-":
        return board[0]
    if board[1] == board[4] == board[7] != "-":
        return board[1]
    if board[2] == board[5] == board[8] != "-":
        return board[2]

    if board[0] == board[4] == board[8] != "-":
        return board[0]
    if board[2] == board[4] == board[6] != "-":
        return board[2]

    return None

# MINIMAX

def minimax(board, depth, isMaximizing):
    result = check_winner_temp(board)

    if result == "O":
        return 10 - depth
    elif result == "X":
        return depth - 10
    elif "-" not in board:
        return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = "-"
                bestScore = max(bestScore, score)
        return bestScore

    else:
        bestScore = 1000
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = "-"
                bestScore = min(bestScore, score)
        return bestScore

# AI move using minimax

def AI(board):
    bestScore = -1000
    bestMove = 0

    for i in range(9):
        if board[i] == "-":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = "-"

            if score > bestScore:
                bestScore = score
                bestMove = i

    board[bestMove] = "O"

# Switch player

def switchplayer():
    global CurrentPlayer
    if CurrentPlayer == "X":
        CurrentPlayer = "O"
    else:
        CurrentPlayer = "X"

# Game loop

while gameRunning:
    printboard(board)

    if CurrentPlayer == "X":
        playerinput(board)
    else:
        print("AI is thinking...")
        AI(board)

    checkwin()
    checktie(board)

    if gameRunning:
        switchplayer()
