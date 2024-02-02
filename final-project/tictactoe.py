"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state(board_size):
    """
    Returns starting state of the board.
    """
    return [[EMPTY for _ in range(board_size)] for _ in range(board_size)];


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = sum(row.count(EMPTY) for row in board);
    if turn == 0:
        return None;

    elif turn % 2 == 0:
        return O;

    else:
        return X;


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set();

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                action.add((i, j));

    return action;


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError;

    result = copy.deepcopy(board);
    result[action[0]][action[1]] = player(board);
    return result;


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    n = len(board)

    if [X for _ in range(n)] in board:
        return X;

    if [O for _ in range(n)] in board:
        return O;

    for j in range(len(board)):
        if all(board[0][j] == board[i][j] for i in range(n)):
            return board[0][j];

    if all(board[0][0] == board[i][i] for i in range(n)) or all(board[0][n - 1] == board[i][n - 1 - i] for i in range(n)):
        return board[n//2][n//2];

    return None;



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if sum(row.count(EMPTY) for row in board) == 0 or winner(board):
        return True;

    else:
        return False;


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1;

        elif winner(board) == O:
            return -1;

        else:
            return 0;


def minimax(board):

    values = [];
    for action in actions(board):
        if terminal(board):
            values.append(utility(board));

        if player(board) == X:
            value, _ = max_value(board);
            values.append(value);

        else:
            value, _ = min_value(board);
            values.append(value);

    return values;

def max_value(board):
    if terminal(board):
        return utility(board), None;

    max_value = float("-inf");
    move = None;
    for action in actions(board):
        value, _ = min_value(result(board, action));
        if value == 1:
            yield value, action;

        if value > max_value:
            max_value = value;
            move = action;

    return max_value, move;

def min_value(board):
    if terminal(board):
        return utility(board), None;


    min_value = float("inf");
    move = None;
    for action in actions(board):
        value, _ = max_value(result(board, action));
        if value == -1:
            yield value, action;

        if value < min_value:
            min_value = value;
            move = action;

    return min_value, move;

def main():
    board_size = int(input("Board Size"));
    board = initial_state(board_size);

    value = {};
    for action in actions(board):
        value[action] = minimax(result(board, action));

main()