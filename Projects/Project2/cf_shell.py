# cf_shell.py
#
# ICS 32A Fall 2023
# Project #2: Send Me On My Way

'''
This module contains the functions that made up the user interface
of a connectfour game in python shell.
'''

import connectfour
import cf_shared

# This is a protected function, will only be used within the module
# to help makeinh other function.

def _who_won(game_status: connectfour.GameState) -> int:
    ''' 
    Returns the number representing either "red" or "yellow" player
    when there is a winner, and prints out the winning statement.
    '''
    winner = connectfour.winner(game_status)
    if winner == 1:
        print('Red Won!')
    elif winner == 2:
        print('Yellow Won!')
    return winner


def run() -> None:
    '''
    Composes and outputs the user interface of the connectfour game
    through python shell: Correct input format, ask for user input, 
    print out game board, etc.
    '''
    column = cf_shared.get_column()
    row = cf_shared.get_row()
    winner = 0

    game_status = cf_shared.start_new_game(column, row)

    print('Please enter your next move in the following format:')
    print('DROP/POP + Column number')
    print('Ex. DROP 5 \n')

    while winner == 0:
        cf_shared.turn(game_status)
        next_move = input('Next Move: ').split()
        game_status = cf_shared.drop_pop(game_status, next_move)
        cf_shared.print_board(game_status, column, row)
        winner = _who_won(game_status)
    

if __name__ == '__main__':
    run()