# project4.py
#
# ICS 32A Fall 2023
# Project 4: The Fall of the World's Own Optimist (Part 1)

import faller
import state
import match

'''
This program takes in the user input, and present
the game Columns on the python shell.
'''

def run() -> None:
    '''
    Implementing the game mechanics, making the game proceeds
    until the game is over or the user ends the game.
    '''
    row_num = int(input())
    column_num = int(input())

    game_board = state.State(row_num, column_num)
    the_board = game_board.new_game()

    state.State.gravity(the_board)
    original = [row[:] for row in the_board]

    # As long as there are matching jewels, keep matching after gravity is applied.
    while True:
        match_check = match.Match(the_board)
        the_board = match_check.vertical()
        the_board = match_check.horizontal()
        state.State.display(the_board)

        # Stop matching when there are no more matching jewels on the board.
        if original == the_board:
            break

        the_board = match.Match.clear_match(the_board)
        enter = input()
        while True:
            if enter == '': break
        state.State.gravity(the_board)
        original = [row[:] for row in the_board]
    

    while True:
        command = input()
        # Quit the game when user inputs 'Q'
        while command.startswith('F') == False and command != 'Q':
            command = input()
        
        if command == 'Q':
            quit()
        
        create_faller = command.split()
        
        the_faller = faller.Faller(the_board, int(create_faller[1]), create_faller[2], create_faller[3], create_faller[4])
        the_board = the_faller.new_drop()
        row = 2
        if faller.Faller.not_bottom(the_board, row+1, the_faller.return_column()) == False:
            pass
        else:
            while True:
                the_board = the_faller.drop(row)
                if row+1 == len(the_board)-1 or faller.Faller.not_bottom(the_board, row+2, the_faller.return_column()) == False:
                    break
                row += 1
            the_board = the_faller.freeze(row)

        original = [row[:] for row in the_board]

        while True:
            match_check = match.Match(the_board)
            the_board = match_check.vertical()
            the_board = match_check.horizontal()
            state.State.display(the_board)

            if original == the_board:
                break

            the_board = match.Match.clear_match(the_board)
            enter = input()
            while True:
                if enter == '': break
            state.State.gravity(the_board)
            original = [row[:] for row in the_board]




if __name__ == '__main__':
    run()