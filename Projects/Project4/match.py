# match.py
#
# ICS 32A Fall 2023
# Project 4: The Fall of the World's Own Optimist (Part 1)

# Contains all the functions that match the jewels, both vertically and horizontally.
class Match:
    def __init__(self, game_state: list[list[str]]):
        '''
        Takes in the current game board, to check if there's any matching jewels.
        '''
        self._state = game_state

    def vertical(self) -> list[list[str]]:
        '''
        Check every single jewel on board to see if any of them can match vertically.
        For jewels at top row, only check downwards, for jewels at bottom row, only check
        upwards. For jewels in the middle, check in both directions.
        '''
        board = self._state
        for row in range(0, len(board)):
            for column in range(1, len(board[0])-1):
                # Skip the locations on board that have no jewel.
                if board[row][column] != '   ':
                    if row == 0 and board[row+1][column][1] == board[row][column][1] and board[row+2][column][1] == board[row][column][1]:
                        board[row][column] = f'*{board[row][column][1]}*'
                        board[row+1][column] = f'*{board[row][column][1]}*'
                        board[row+2][column] = f'*{board[row][column][1]}*'
                        row_conti = row + 2
                        while row_conti < len(board)-1 and board[row_conti + 1][column] == board[row][column][1]:
                            board[row_conti + 1][column] = f'*{board[row][column][1]}*'
                            row_conti += 1
                    elif row == len(board) -1 and board[row-1][column][1] == board[row][column][1] and board[row-2][column][1] == board[row][column][1]:
                        board[row][column] = f'*{board[row][column][1]}*'
                        board[row-1][column] = f'*{board[row][column][1]}*'
                        board[row-2][column] = f'*{board[row][column][1]}*'
                        row_conti = row - 2
                        while row_conti > 0 and board[row_conti -1 ][column] == board[row][column][1]:
                            board[row_conti - 1][column] = f'*{board[row][column][1]}*'
                            row_conti -= 1
                    elif row != 0 and row != len(board)-1 and board[row-1][column][1] == board[row][column][1] and board[row+1][column][1] == board[row][column][1]:
                        board[row][column] = f'*{board[row][column][1]}*'
                        board[row-1][column] = f'*{board[row][column][1]}*'
                        board[row+1][column] = f'*{board[row][column][1]}*'
                        row_up = row - 1
                        row_down = row + 1
                        while row_up > 0 and board[row_up-1][column][1] == board[row][column][1]:
                            board[row_up-1][column] = f'*{board[row][column][1]}*'
                            row_up -= 1
                        while row_down < len(board)-1 and board[row_down+1][column][1] == board[row][column][1]:
                            board[row_down+1][column] = f'*{board[row][column][1]}*'
                            row_down += 1
        
        return board

    def horizontal(self) -> list[list[str]]:
        '''
        Check every single jewel on board to see if any of them can match horizontally.
        For jewels at the most left edge, only check to the right, for jewels at the most right edge, row, 
        only check to the left. For jewels in the middle, check in both directions.
        '''
        board = self._state
        for  column in range(1, len(board[0])-1):
            for row in range(0, len(board)):
                # Skip the locations on board that have no jewel.
                if board[row][column] != '   ':
                    if column == 1 and board[row][column+1][1] == board[row][column][1] and board[row][column+2][1] == board[row][column][1]:
                        board[row][column] = f'*{board[row][column][1]}*'
                        board[row][column+1] = f'*{board[row][column][1]}*'
                        board[row][column+2] = f'*{board[row][column][1]}*'
                        col_conti = column + 2
                        while col_conti < len(board[0])-1 and board[row][col_conti+1] == board[row][column][1]:
                            board[row][col_conti+1] = f'*{board[row][column][1]}*'
                            col_conti += 1
                    elif column == len(board[0])-2 and board[row][column-1][1] == board[row][column][1] and board[row][column-2][1] == board[row][column][1]:
                        board[row][column] = f'*{board[row][column][1]}*'
                        board[row][column-1] = f'*{board[row][column][1]}*'
                        board[row][column-2] = f'*{board[row][column][1]}*'
                        col_conti = column - 2
                        while col_conti > 1 and board[row][col_conti-1] == board[row][column][1]:
                            board[row][col_conti-1] = f'*{board[row][column][1]}*'
                            col_conti -= 1
                    elif column != 1 and column != len(board[0])-2 and board[row][column-1][1] == board[row][column][1] and board[row][column+1][1] == board[row][column][1]:
                        board[row][column] = f'*{board[row][column][1]}*'
                        board[row][column-1] = f'*{board[row][column][1]}*'
                        board[row][column+1] = f'*{board[row][column][1]}*'
                        col_left = column - 1
                        col_right = column + 1
                        while col_left > 1 and board[row][col_left-1][1] == board[row][column][1]:
                            board[col_left-1][column] = f'*{board[row][column][1]}*'
                            col_left -= 1
                        while col_right < len(board[0])-2 and board[row][col_right+1][1] == board[row][column][1]:
                            board[row][col_right+1] = f'*{board[row][column][1]}*'
                            col_right += 1
        
        return board


    def clear_match(board: list[list[str]]) -> list[list[str]]:
        '''
        Remove all the matched jewels and replace them with blank.
        '''
        for row in range(0, len(board)):
            for column in range(0, len(board[0])):
                # if an element contains '*', replace it with blank.
                if '*' in board[row][column]:
                    board[row][column] = '   '

        return board

