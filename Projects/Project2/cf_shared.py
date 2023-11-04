# cf_shared.py
#
# ICS 32A Fall 2023
# Project #2: Send Me On My Way

'''
This module contains the functions that will be used in both user interfaces,
for python shell version of connectfour and networked version of connectfour.
'''

import connectfour

# These are the public functions that could be called when the module is imported.

def get_column() -> int:
    '''
    This function asks the user for the number of columns in game board.
    The input needs to be valid.
    '''
    while True:
        input_column = input('The column of the gameboard (between 4 and 20): ')

        if len(input_column) == 0 or input_column.isspace() == True or input_column.isnumeric() == False:
            print('Invalid input, please try again.')
        elif 4 <= int(input_column) <= 20:
            break
        else: 
            print('Invalid input, please try again.')

    return int(input_column)


def get_row() -> int:
    '''
    This function asks the user for the number of rows in game board.
    The input needs to be valid.
    '''
    while True:
        input_row = input('The row of the gameboard (between 4 and 20): ')

        if len(input_row) == 0 or input_row.isspace() == True or input_row.isnumeric() == False:
            print('Invalid input, please try again.')
        elif 4 <= int(input_row) <= 20:
            break
        else: 
            print('Invalid input, please try again.')

    return int(input_row)


def start_new_game(column: int, row: int) -> connectfour.GameState:
    '''
    Creates and prints a new game board when a new game started.
    In the correct format with number of columns on the top of game board.
    '''
    game_status = connectfour.new_game(column, row)
    new_board = ''
    _print_column_nums(column)
    for num1 in range(0, row):
        print(new_board)
        new_board = ''
        for num2 in range(0, column):
            new_board = new_board + '.' + '  '
    print(new_board)
    return game_status
    

def drop_pop(game_status: connectfour.GameState, next_move: list) -> connectfour.GameState:
    '''
    Drops or Pops at certain positionaccording to the user input, keep asking for valid inputs 
    if the position asked for drop/pop is invalid.
    '''
    while True:
        try:    
            if next_move[0] == 'DROP':
                game_status = connectfour.drop(game_status, int(next_move[1])-1)
            elif next_move[0] == 'POP':
                game_status = connectfour.pop(game_status, int(next_move[1])-1)
            else:
                raise ValueError
            break
        except:
            print('Invalid input, please try again.')
            next_move = input('Next Move: ').split()
    
    return game_status


def print_board(game_status: connectfour.GameState, column: int, row: int) -> None:
    '''
    Prints out the game board in the correct format, with number of columns on the top of game board.
    '''
    board = ''
    _print_column_nums(column)

    for num1 in range(0, row):
        print(board)
        board = ''
        for num2 in range(0, column):
            if game_status[0][num2][num1] == 0:
                board = board + '.' + '  '
            elif game_status[0][num2][num1] == 1:
                board = board + 'R' + '  '
            elif game_status[0][num2][num1] == 2:
                board = board + 'Y' + '  '
    print(board)    


def turn(game_status: connectfour.GameState) -> None:
    '''
    Determines and prints who's turn is it (red/yellow).
    '''
    if game_status[1] == 1:
        print("Red's turn")
    elif game_status[1] == 2:
        print("Yellow's turn")


# This is a protected function, it will only be used to 
# help construct other functions within the module.


def _print_column_nums(column: int) -> None:
    '''
    Prints out the column numbers in a row, with
    correct spacing, two space in between single digit 
    numbers, one space for double digits numbers.
    '''
    for i in range(1, column + 1):
        if i < 9:
            print(i, end='  ')
        else: print(i, end=' ')