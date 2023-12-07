# state.py
#
# ICS 32A Fall 2023
# Project 4: The Fall of the World's Own Optimist (Part 1)

# Contains functions that create a new game board, applying gravity to all the jewels on the board,
# and display the board.
class State:
    def __init__(self, row: int, column: int):
        ''' 
        Takes in the row and column number of the new board.
        '''
        self._row = row
        self._column = column

    def new_game(self) -> list[list[str]]:
        '''
        Creates a new game board with the given numbers of row and column.
        '''
        game_state = [[] for _ in range(self._row)]
        type = input()
        if type == 'EMPTY':
            for rows in game_state:
                rows.append('|')
                for i in range(1, self._column + 1):
                    rows.append('   ')
                rows.append('|')
    
        elif type == 'CONTENTS':
            counter = 0
            while counter < self._row:
                game_state[counter].append('|')
                content = input()
                for char in content:
                    if char.isspace():
                        game_state[counter].append('   ')
                    else:
                        game_state[counter].append(f' {char} ')
                game_state[counter].append('|')
                counter += 1
    
        return game_state

    def display(game_state: list[list[str]]) -> None:
        '''
        Displays the game board in correct format.
        '''
        for list in game_state:
            print(''.join(list))
        print(' ' + '---' * (len(game_state[0])-2) + ' ')


    def gravity(game_state: list[list[str]]) -> list[list[str]]:
        '''
        Applies gravity to all the jewels on board, making them drop 
        to the bottom.
        '''
        board = game_state
        for i in range(len(board)-2, -1, -1):
            for j in range(1, len(board[0])-1):
                row = i
                while board[row+1][j] == '   ' and board[row][j] != '   ':
                    board[row+1][j] = board[row][j]
                    board[row][j] = '   '
                    if row != len(board) -2:
                        row += 1
        return board

