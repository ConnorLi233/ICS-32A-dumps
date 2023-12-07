# faller.py
#
# ICS 32A Fall 2023
# Project 4: The Fall of the World's Own Optimist (Part 1)

import state

class InvalidDrop(Exception):
    '''Raised whenever an invalid drop is made, at the invalid column'''
    pass

# Contains functions that create and drop new fallers, move fallers, freeze fallers, etc.
class Faller:
    def __init__(self, game_state: list[list[str]], location: int, faller1: str, faller2: str, faller3: str):
        ''' 
        Takes in the game board, the column to drop the new faller,
        and all three jewels in the new faller.
        '''
        self._state = game_state
        self._location = location
        self._faller1 = faller1
        self._faller2 = faller2
        self._faller3 = faller3

    def not_bottom(board, row, column) -> bool:
        '''
        Check if a given location on the game board is empty,
        (the location below the faller).
        '''
        if board[row][column] == '   ':
            return True
        else: return False

    # list[list[str]] is the type of the game board.
    def _new_right(self, num: int, location: int, board: list[list[str]]) -> list[list[str]]:
        '''
        Moves a new faller to the right at any time before all three jewels are
        on board.
        '''
        if location < len(board[0])-2:
            # Moves the bottom first jewel to the right.
            if num == 1 and board[0][location + 1] == '   ':
                if Faller.not_bottom(board, 0, location+1):
                    board[0][location + 1] = f'[{self._faller3}]'
                    board[0][location] = '   '
                else:
                    board[0][location + 1] = f'|{self._faller3}|'
                    board[0][location] = '   '
                self._location += 1

            # Moves the bottom two jewels to the right.
            elif num == 2 and board[0][location + 1] == '   ' and board[1][location + 1] == '   ':
                if Faller.not_bottom(board, 1, location+1):
                    board[0][location + 1] = f'[{self._faller2}]'
                    board[0][location] = '   '
                    board[1][location + 1] = f'[{self._faller3}]'
                    board[1][location] = '   '
                else:
                    board[0][location + 1] = f'|{self._faller2}|'
                    board[0][location] = '   '
                    board[1][location + 1] = f'|{self._faller3}|'
                    board[1][location] = '   '
                self._location += 1

            # Moves all three jewels to the right.
            elif num == 3 and board[0][location + 1] == '   ' and board[1][location + 1] == '   ' and board[2][location + 1] == '   ':
                if Faller.not_bottom(board, 2, location+1):
                    board[0][location + 1] = f'[{self._faller1}]'
                    board[0][location] = '   '
                    board[1][location + 1] = f'[{self._faller2}]'
                    board[1][location] = '   '
                    board[2][location + 1] = f'[{self._faller3}]'
                    board[2][location] = '   '
                else:
                    board[0][location + 1] = f'|{self._faller1}|'
                    board[0][location] = '   '
                    board[1][location + 1] = f'|{self._faller2}|'
                    board[1][location] = '   '
                    board[2][location + 1] = f'|{self._faller3}|'
                    board[2][location] = '   '
                self._location += 1
        
        return board

    def _new_left(self, num: int, location: int, board: list[list[str]]) -> list[list[str]]:
        '''
        Moves a new faller to the left at any time before all three jewels are
        on board.
        '''
        if location > 1:
            # Moves the bottom first jewel to the left.
            if num == 1 and board[0][location - 1] == '   ':
                if Faller.not_bottom(board, 0, location-1):
                    board[0][location - 1] = f'[{self._faller3}]'
                    board[0][location] = '   '
                else:
                    board[0][location - 1] = f'|{self._faller3}|'
                    board[0][location] = '   '
                self._location -= 1
            
            # Moves the bottom two jewels to the left.
            elif num == 2 and board[0][location - 1] == '   ' and board[1][location - 1] == '   ':
                if Faller.not_bottom(board, 1, location-1):
                    board[0][location - 1] = f'[{self._faller2}]'
                    board[0][location] = '   '
                    board[1][location - 1] = f'[{self._faller3}]'
                    board[1][location] = '   '
                else:
                    board[0][location - 1] = f'|{self._faller2}|'
                    board[0][location] = '   '
                    board[1][location - 1] = f'|{self._faller3}|'
                    board[1][location] = '   '
                self._location -= 1

            # Moves all three jewels to the left.
            elif num == 3 and board[0][location - 1] == '   ' and board[1][location - 1] == '   ' and board[2][location - 1] == '   ':
                if Faller.not_bottom(board, 2, location-1):
                    board[0][location - 1] = f'[{self._faller1}]'
                    board[0][location] = '   '
                    board[1][location - 1] = f'[{self._faller2}]'
                    board[1][location] = '   '
                    board[2][location - 1] = f'[{self._faller3}]'
                    board[2][location] = '   '
                else:
                    board[0][location - 1] = f'|{self._faller1}|'
                    board[0][location] = '   '
                    board[1][location - 1] = f'|{self._faller2}|'
                    board[1][location] = '   '
                    board[2][location - 1] = f'|{self._faller3}|'
                    board[2][location] = '   '
                self._location -= 1

        return board
    
    def _right(self, row: int, location: int, board: list[list[str]]) -> list[list[str]]:
        '''
        After a faller is fully on board (all three jewels present), moves it to the right 
        any time before it freezes.
        '''
        if location < len(board[0])-2 and row < len(board)-1:
            if board[row-1][location + 1] == '   ' and board[row][location + 1] == '   ' and board[row+1][location + 1] == '   ':
                if row == len(board) - 2 or Faller.not_bottom(board, row+2, location+1) == False:
                    board[row-1][location + 1] = f'|{self._faller1}|'
                    board[row-1][location] = '   '
                    board[row][location + 1] = f'|{self._faller2}|'
                    board[row][location] = '   '
                    board[row+1][location + 1] = f'|{self._faller3}|'
                    board[row+1][location] = '   '
                    self._location += 1
                else:
                    board[row-1][location + 1] = f'[{self._faller1}]'
                    board[row-1][location] = '   '
                    board[row][location + 1] = f'[{self._faller2}]'
                    board[row][location] = '   '
                    board[row+1][location + 1] = f'[{self._faller3}]'
                    board[row+1][location] = '   '
                    self._location += 1

        return board

    def _left(self, row: int, location: int, board: list[list[str]]) -> list[list[str]]:
        '''
        After a faller is fully on board (all three jewels present), moves it to the left 
        any time before it freezes.
        '''
        if location > 1 and row < len(board)-1:
            if board[row-1][location - 1] == '   ' and board[row][location - 1] == '   ' and board[row+1][location - 1] == '   ':
                if row == len(board) - 2 or Faller.not_bottom(board, row+2, location-1) == False:
                    board[row-1][location - 1] = f'|{self._faller1}|'
                    board[row-1][location] = '   '
                    board[row][location - 1] = f'|{self._faller2}|'
                    board[row][location] = '   '
                    board[row+1][location - 1] = f'|{self._faller3}|'
                    board[row+1][location] = '   '
                    self._location -= 1
                else:
                    board[row-1][location - 1] = f'[{self._faller1}]'
                    board[row-1][location] = '   '
                    board[row][location - 1] = f'[{self._faller2}]'
                    board[row][location] = '   '
                    board[row+1][location - 1] = f'[{self._faller3}]'
                    board[row+1][location] = '   '
                    self._location -= 1
                    
        return board

    def _new_rotate(self) -> None:
        '''
        Rotates a new faller.
        '''
        swap = self._faller3
        self._faller3 = self._faller2
        self._faller2 = self._faller1
        self._faller1 = swap

    def _rotate(self, row: int) -> list[list[str]]:
        '''
        Rotates a faller (All three jewels fully present on board for a round).
        '''
        swap1 = self._state[row+1][self._location]
        self._state[row+1][self._location] = self._state[row][self._location]
        self._state[row][self._location] = self._state[row-1][self._location]
        self._state[row-1][self._location] = swap1

        swap = self._faller3
        self._faller3 = self._faller2
        self._faller2 = self._faller1
        self._faller1 = swap
    
        return self._state

    def _new_move(self, faller_num: int, enter: str) -> list[list[str]]:
        '''
        Determines the move to a new faller according to the user input.
        '''
        if enter == '>' and self._location < len(self._state[0])-2:
            self._state = self._new_right(faller_num, self._location, self._state)
        elif enter == '<' and self._location > 1:
            self._state = self._new_left(faller_num, self._location, self._state)
        elif enter == 'R':
            self._new_rotate()

        return self._state
    
    def _move(self, row: int, enter: str) -> list[list[str]]:
        '''
        Determines the move to a faller according to the user input.
        '''
        if enter == '>':
            self._state = self._right(row, self._location, self._state)
            state.State.display(self._state)
        elif enter == '<':
            self._state = self._left(row, self._location, self._state)
            state.State.display(self._state)
        elif enter == 'R':
            self._state = self._rotate(row)
            state.State.display(self._state)

        return self._state
                

    def new_drop(self) -> list[list[str]]:
        '''
        Drops a new faller, one at a time into the board.
        '''
        if self._location < len(self._state[0])-1 and self._location > 0:
            # If the board is full before the first jewel enters the board,
            # game ends.
            if Faller.not_bottom(self._state, 0, self._location) == False:
                state.State.display(self._state)
                print('GAME OVER')
                quit()

            # First jewel enters, keep taking in moves (>,<,R) until the user hit enter to proceed.
            while True:      
                if Faller.not_bottom(self._state, 1, self._location):
                    self._state[0][self._location] = f'[{self._faller3}]'
                    state.State.display(self._state)
                    enter = input()
                    self._state = self._new_move(1, enter)

                if Faller.not_bottom(self._state, 1, self._location) == False:
                    self._state[0][self._location] = f'|{self._faller3}|'
                    state.State.display(self._state)
                    enter = input()
                    self._state = self._new_move(1, enter)

                if enter == 'Q':
                    quit()
                if enter == "":
                    break
            
            # If the board is full before the second jewel enters the board,
            # game ends.
            if Faller.not_bottom(self._state, 1, self._location) == False :
                self._state[0][self._location] = f' {self._faller3} '
                state.State.display(self._state)
                print('GAME OVER')
                quit()               
            
            # Second jewel enters, keep taking in moves (>,<,R) until the user hit enter to proceed.
            while True:         
                if Faller.not_bottom(self._state, 2, self._location):
                    self._state[0][self._location] = f'[{self._faller2}]'
                    self._state[1][self._location] = f'[{self._faller3}]'
                    state.State.display(self._state)
                    enter = input()
                    self._state = self._new_move(2, enter)

                elif Faller.not_bottom(self._state, 2, self._location) == False:
                    self._state[0][self._location] = f'|{self._faller2}|'
                    self._state[1][self._location] = f'|{self._faller3}|'
                    state.State.display(self._state)
                    enter = input()
                    self._state = self._new_move(2, enter)
            
                if enter == 'Q':
                    quit()
                if enter == "":
                    break
                    
            # If the board is full before the third jewel enters the board,
            # game ends.
            if Faller.not_bottom(self._state, 2, self._location) == False:
                self._state[0][self._location] = f' {self._faller2} '
                self._state[1][self._location] = f' {self._faller3} '
                state.State.display(self._state)
                print('GAME OVER')
                quit()

            # Third jewel enters, keep taking in moves (>,<,R) until the user hit enter to proceed.
            while True:      
                if Faller.not_bottom(self._state, 3, self._location):
                    self._state[0][self._location] = f'[{self._faller1}]'
                    self._state[1][self._location] = f'[{self._faller2}]'
                    self._state[2][self._location] = f'[{self._faller3}]'
                    state.State.display(self._state)
                    enter = input()
                    self._state = self._new_move(3, enter)

                elif Faller.not_bottom(self._state, 3, self._location) == False:
                    self._state[0][self._location] = f'|{self._faller1}|'
                    self._state[1][self._location] = f'|{self._faller2}|'
                    self._state[2][self._location] = f'|{self._faller3}|'
                    state.State.display(self._state)
                    enter = input()
                    self._state = self._new_move(3, enter)           
            
                if enter == 'Q':
                    quit()
                if enter == "":
                    break
                    
            # If the new faller can't move down any more, and user hits enter to proceed, freeze it.
            if Faller.not_bottom(self._state, 3, self._location) == False:
                self._state[0][self._location] = f' {self._faller1} '
                self._state[1][self._location] = f' {self._faller2} '
                self._state[2][self._location] = f' {self._faller3} '
                
        else:
            raise InvalidDrop()

        return self._state
    
    def drop(self, row: int) -> list[list[str]]:
        '''
        Drops a faller by one space down, including all three jewels.
        '''
        if row+1 == len(self._state)-1 or Faller.not_bottom(self._state, row+2, self._location) == False:
            self._state[row-1][self._location] = f'|{self._faller1}|'
            self._state[row][self._location] = f'|{self._faller2}|'
            self._state[row+1][self._location] = f'|{self._faller3}|'
            self._state[row-2][self._location] = '   '
            state.State.display(self._state)
            while True:
                enter = input()
                self._move(row, enter)

                if enter == 'Q':
                    quit()
                if enter == '':
                    break
                    
        elif Faller.not_bottom(self._state, row+1, self._location):
            self._state[row-1][self._location] = f'[{self._faller1}]'
            self._state[row][self._location] = f'[{self._faller2}]'
            self._state[row+1][self._location] = f'[{self._faller3}]'
            self._state[row-2][self._location] = '   '
            state.State.display(self._state)
            while True:
                enter = input()
                self._move(row, enter)
                if enter == 'Q':
                    quit()
                if enter == '':
                    break
    
        return self._state
       
    def freeze(self, row: int) -> list[list[str]]:
        '''
        Freezes a faller when it reaches the bottom.
        '''
        self._state[row-1][self._location] = f' {self._faller1} '
        self._state[row][self._location] = f' {self._faller2} '
        self._state[row+1][self._location] = f' {self._faller3} '

        return self._state

    def return_column(self) -> int:
        '''
        Returns the current column number of the faller.
        '''
        return self._location
       





        
