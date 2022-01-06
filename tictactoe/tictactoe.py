"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_pieces = 0
    for row in board:
        for col in row:
            if col != EMPTY:
                num_pieces += 1
    return X if num_pieces % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                yield (row, col)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p = player(board)
    row, col = action
    if board[row][col] != EMPTY:
        raise Exception("Invalid action")
    
    result_board = [row[:] for row in board]
    result_board[row][col] = p
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if len(set(row)) == 1:
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        vals = set()
        for row in range(len(board)):
            vals.add(board[row][col])
        if len(vals) == 1:
            return board[0][col]

    # Check diagonals
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]

    # Draw
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if there is a winner
    w = winner(board)
    if w is not None:
        return True

    # Check if there are any empty spaces
    for row in board:
        for col in row:
            if col is EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w is X:
        return 1
    elif w is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    p = player(board)
    if p == X:
        action, _ = max_value(board)
    else:
        action, _ = min_value(board)
    return action

def max_value(board):
    if terminal(board):
        return None, utility(board)

    v = float("-inf")
    best_action = None
    for action in actions(board):
        _, min_v = min_value(result(board, action))
        if min_v > v:
            v = min_v
            best_action = action
    return best_action, v

def min_value(board):
    if terminal(board):
        return None, utility(board)
    
    v = float("inf")
    best_action = None
    for action in actions(board):
        _, max_v = max_value(result(board, action))
        if max_v < v:
            v = max_v
            best_action = action
    return best_action, v