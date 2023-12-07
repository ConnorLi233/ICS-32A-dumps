# columns.py
#
# ICS 32A Fall 2023
# Project 5: The Fall of the World's Own Optimist (Part 2)

'''
This module includes the game mechanics of the Columns game. Including creating new fallers,
drop fallers and making moves.
'''

import random

class State:
    def __init__(self):
        ''' 
        Creates a 2D list with 13 rows and 6 columns.
        '''
        self._state = [[], [], [], [], [], [], [], [], [], [], [], [], []]


    def new_game(self) -> list[list[str]]:
        '''
        Creates a new game board with 13 rows and 6 columns.
        '''
        board = self._state
        for row in board:
            for i in range(6):
                row.append('   ')
        
        self._state = board
        return self._state


class Faller:
    def __init__(self, game_state: list[list[str]], col: int, faller1: int, faller2: int, faller3: int):
        ''' 
        Takes in the game board, the column to drop the new faller,
        and all three jewels in the new faller (will be randomized).
        '''
        self._col = col
        self._faller1 = faller1
        self._faller2 = faller2
        self._faller3 = faller3
        self._state = game_state
        self._fit = True
        

    def not_bottom(board, row, column) -> bool:
        '''
        Check if a given location on the game board is empty,
        (the location below the faller).
        '''
        if board[row][column] == '   ':
            return True
        else: return False


    # list[list[str]] is the type of the game board.
    def new_right(self, num: int) -> list[list[str]]:
        '''
        Moves a new faller to the right at any time before all three jewels are
        on board.
        '''
        if self._col < len(self._state[0])-1:
            # Moves the bottom first jewel to the right.
            if num == 1 and self._state[0][self._col + 1] == '   ':
                self._state[0][self._col + 1] = self._faller3
                self._state[0][self._col] = '   '
                self._col += 1

            # Moves the bottom two jewels to the right.
            elif num == 2 and self._state[0][self._col + 1] == '   ' and self._state[1][self._col + 1] == '   ':
                self._state[0][self._col + 1] = self._faller2
                self._state[0][self._col] = '   '
                self._state[1][self._col + 1] = self._faller3
                self._state[1][self._col] = '   '

                self._col += 1

            # Moves all three jewels to the right.
            elif num == 3 and self._state[0][self._col + 1] == '   ' and self._state[1][self._col + 1] == '   ' and self._state[2][self._col + 1] == '   ':
                self._state[0][self._col + 1] = self._faller1
                self._state[0][self._col] = '   '
                self._state[1][self._col + 1] = self._faller2
                self._state[1][self._col] = '   '
                self._state[2][self._col + 1] = self._faller3
                self._state[2][self._col] = '   '
                self._col += 1
        
        return self._state


    def new_left(self, num: int) -> list[list[str]]:
        '''
        Moves a new faller to the left at any time before all three jewels are
        on board.
        '''
        if self._col > 0:
            # Moves the bottom first jewel to the left.
            if num == 1 and self._state[0][self._col - 1] == '   ':
                self._state[0][self._col - 1] = self._faller3
                self._state[0][self._col] = '   '
                self._col -= 1
            
            # Moves the bottom two jewels to the left.
            elif num == 2 and self._state[0][self._col - 1] == '   ' and self._state[1][self._col - 1] == '   ':
                self._state[0][self._col - 1] = self._faller2
                self._state[0][self._col] = '   '
                self._state[1][self._col - 1] = self._faller3
                self._state[1][self._col] = '   '
                self._col -= 1

            # Moves all three jewels to the left.
            elif num == 3 and self._state[0][self._col - 1] == '   ' and self._state[1][self._col - 1] == '   ' and self._state[2][self._col - 1] == '   ':
                self._state[0][self._col - 1] = self._faller1
                self._state[0][self._col] = '   '
                self._state[1][self._col - 1] = self._faller2
                self._state[1][self._col] = '   '
                self._state[2][self._col - 1] = self._faller3
                self._state[2][self._col] = '   '
                self._col -= 1

        return self._state
    
    
    def right(self, row: int) -> list[list[str]]:
        '''
        After a faller is fully on board (all three jewels present), moves it to the right 
        any time before it freezes.
        '''
        if self._col < len(self._state[0])-1 and row < len(self._state):
            if self._state[row-1][self._col + 1] == '   ' and self._state[row][self._col + 1] == '   ' and self._state[row+1][self._col + 1] == '   ':
                self._state[row-1][self._col + 1] = self._faller1
                self._state[row-1][self._col] = '   '
                self._state[row][self._col + 1] = self._faller2
                self._state[row][self._col] = '   '
                self._state[row+1][self._col + 1] = self._faller3
                self._state[row+1][self._col] = '   '  
                self._col += 1
        
        return self._state
    

    def left(self, row: int) -> list[list[str]]:
        '''
        After a faller is fully on board (all three jewels present), moves it to the left 
        any time before it freezes.
        '''
        if self._col > 0 and row < len(self._state):
            if self._state[row-1][self._col - 1] == '   ' and self._state[row][self._col - 1] == '   ' and self._state[row+1][self._col - 1] == '   ':
                self._state[row-1][self._col - 1] = self._faller1
                self._state[row-1][self._col] = '   '
                self._state[row][self._col - 1] = self._faller2
                self._state[row][self._col] = '   '
                self._state[row+1][self._col - 1] = self._faller3
                self._state[row+1][self._col] = '   '
                self._col -= 1

        return self._state
    

    def new_rotate(self, fl_num: int) -> None:
        '''
        Rotates a new faller.
        '''
        swap = self._faller3
        self._faller3 = self._faller2
        self._faller2 = self._faller1
        self._faller1 = swap

        if fl_num == 1:
            self._state[0][self._col] = self._faller3
        elif fl_num == 2: 
            self._state[0][self._col] = self._faller2
            self._state[1][self._col] = self._faller3
        elif fl_num == 3: 
            self._state[0][self._col] = self._faller1
            self._state[1][self._col] = self._faller2
            self._state[2][self._col] = self._faller3

        return self._state


    def rotate(self, row: int) -> list[list[str]]:
        '''
        Rotates a faller (All three jewels fully present on board for a round).
        '''

        swap = self._faller3
        self._faller3 = self._faller2
        self._faller2 = self._faller1
        self._faller1 = swap

        self._state[row-1][self._col] = self._faller1
        self._state[row][self._col] = self._faller2
        self._state[row+1][self._col] = self._faller3


        return self._state


    def create_faller(self) -> None:
        '''
        Creates a new faller with randomized color, and starts dropping at a random column that is not full
        '''
        self._col = random.randint(0,5)
        while Faller.not_bottom(self._state, 0, self._col) == False and '   ' in self._state[0]:
            # Keep randomizing the drop column if it is full, until a column that is not full gets selected.
            self._col = random.randint(0,5)
        self._faller1 = random.randint(1,7)
        self._faller2 = random.randint(1,7)
        self._faller3 = random.randint(1,7)


    def new_drop(self, fl_num: int) -> list[list[str]]:
        '''
        Drops a new faller, one at a time into the board.
        '''
        
        # If the board is full before the first jewel enters the board,
        # game ends.
        if fl_num == 0:
            if Faller.not_bottom(self._state, 0, self._col) == False:
                self._fit = False

            # First jewel enters.
            else:
                self._state[0][self._col] = self._faller3
        
        if fl_num == 1:
            # If the board is full before the second jewel enters the board,
            # game ends.
            if Faller.not_bottom(self._state, 1, self._col) == False :
                self._fit = False
            
            # Second jewel enters.
            else:
                self._state[0][self._col] = self._faller2
                self._state[1][self._col] = self._faller3

        if fl_num == 2:
            # If the board is full before the third jewel enters the board,
            # game ends.
            if Faller.not_bottom(self._state, 2, self._col) == False:
                self._fit = False

            # Third jewel enters.
            else:
                self._state[0][self._col] = self._faller1
                self._state[1][self._col] = self._faller2
                self._state[2][self._col] = self._faller3

        return self._state
    
    def drop(self, row: int) -> list[list[str]]:
        '''
        Drops a faller by one space down, including all three jewels.
        '''                
        if Faller.not_bottom(self._state, row+1, self._col) and row < 12:
            self._state[row-1][self._col] = self._faller1
            self._state[row][self._col] = self._faller2
            self._state[row+1][self._col] = self._faller3
            self._state[row-2][self._col] = '   '

        return self._state
    

    def return_column(self) -> int:
        '''
        Returns the current column number of the faller.
        '''
        return self._col
    
    
    def fit(self) -> bool:
        '''
        Returns if all three jewels of a new faller can fit into the board.
        '''
        return self._fit



