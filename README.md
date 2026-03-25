# Tic Tac Toe

This project is a command-line Tic Tac Toe game written in Python where a human player (X) plays against an AI (O). The AI uses the Minimax algorithm to always choose the optimal move.

## AI Overview

The AI is implemented using the Minimax algorithm, a standard decision-making technique used in turn-based games. It evaluates all possible future moves and selects the one that gives the best outcome.

The algorithm assumes:

The AI plays optimally
The opponent also plays optimally
How the AI Works
1. Game State Evaluation

The function check_winner_temp(board) is used to evaluate the board safely without modifying the actual game.

It returns:

"O" if the AI wins
"X" if the player wins
None if the game is still ongoing
2. Minimax Function
def minimax(board, depth, isMaximizing):

This function recursively explores all possible game states.

Base Cases:
If AI wins → returns 10 - depth
If player wins → returns depth - 10
If tie → returns 0

Depth is used to:

Prefer faster wins
Delay losses
3. Maximizing and Minimizing
AI (O) is the maximizing player and tries to maximize the score
Human (X) is the minimizing player and tries to minimize the score
4. Backtracking

Each move is:

Applied temporarily
Evaluated using recursion
Undone after evaluation

This ensures the original board state is preserved.

5. Choosing the Best Move
def AI(board):


