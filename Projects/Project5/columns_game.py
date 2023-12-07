# columns_game.py
#
# ICS 32A Fall 2023
# Project 5: The Fall of the World's Own Optimist (Part 2)

'''
This program is the view of the game, including the GUI of the Columns game, 
and process user inputs.
'''

import pygame
import columns
import time

class ColumnsGame:
    def __init__(self):
        self._running = True
        self._state = columns.State().new_game()
        self._new_faller = columns.Faller(self._state, 0, 0, 0, 0)
        self._colors = {1: pygame.Color(252, 3, 3),
                        2: pygame.Color(252, 145, 5),
                        3: pygame.Color(252, 252, 5),
                        4: pygame.Color(5, 252, 30),
                        5: pygame.Color(5, 252, 240),
                        6: pygame.Color(5, 30, 252),
                        7: pygame.Color(130, 0, 252)}
        self._fl_num = 0
        self._row = 2


    def run(self) -> None:
        '''
        Runs the game, uses other functions to visualize the game through pygame window.
        '''
        pygame.init()

        self._create_board((600, 800))
        font = pygame.font.Font('freesansbold.ttf', 63)

        text = font.render('Landed!', True, (0, 204, 0))
        text_position = (self._surface.get_width()/4, self._surface.get_height()/6)

        game_over = font.render('GAME OVER', True, 'red')

        clock = pygame.time.Clock()
        counter = 0

        while self._running:
            clock.tick(10)
            counter += 1
            # Takes in user input/actions, respond to them accordingly.
            self._handle_events()    
                
            if counter == 10:
                if self._fl_num < 3: 
                    # If the faller just got created and has not fully presented in board yet, drop it into the baord one by one.   
                    if self._fl_num == 0:
                        self._new_faller.create_faller()
                    if self._new_faller.fit():
                        self._state = self._new_faller.new_drop(self._fl_num)
                        self._draw_board()
                    else:
                        # If the board is full, end the game by switching to a "GAME OVER" screen.
                        surface = pygame.display.get_surface()
                        surface.fill(pygame.Color(255, 255, 0))
                        surface.blit(game_over, text_position)
                        pygame.display.flip()
                        time.sleep(3)
                        pygame.quit()
            
                    self._fl_num += 1

                else:
                    # After the new faller has fully presented in the board, drop all three jewels at once.
                    self._state = self._new_faller.drop(self._row)

                    self._draw_board()

                    if self._row < 11:
                        self._row += 1

                if columns.Faller.not_bottom(self._state, self._row+1, self._new_faller.return_column()) == False and self._row != 0 and self._row != 1 and self._row != 2:
                    # Visual cue: display the text "Landed!" when the faller landed.
                    self._surface.blit(text, text_position)
                    pygame.display.flip()
                    time.sleep(0.2)
                    self._row = 2
                    self._fl_num = 0
                counter = 0                            

        pygame.quit()


    def _create_board(self, size: tuple[int, int]) -> None:
        '''
        Creates an obejct for the surface we'll diaplay, make it resizable.
        '''
        self._surface = pygame.display.set_mode(size, pygame.RESIZABLE)
    

    def _draw_board(self):
        '''
        Visualize the board with background and colors.
        '''
        height = self._surface.get_height()
        width = self._surface.get_width()
        height_divided = height * 1/13
        width_divided = width * 1/6

        for y in range(13):
            row = y
            y = y * 1/13
            for x in range(6):
                column = x
                x = x * 1/6
                if self._state[row][column] == '   ':     
                    # If there's no element at the position, display it as the background color.   
                    pygame.draw.rect(self._surface, 'black', (x * width, y * height, width_divided, height_divided))
                    pygame.draw.rect(self._surface, 'blue', (x * width, y * height, width_divided, height_divided),1)
                    self._draw_frame()
                else:
                    # If there's an element at the position, diaplay the jewel with the corresponding color.
                    pygame.draw.rect(self._surface, self._colors[self._state[row][column]], (x * width, y * height, width_divided, height_divided))
                    pygame.draw.rect(self._surface, 'white', (x * width, y * height, width_divided, height_divided),2)
                    self._draw_frame()


    def _draw_frame(self) -> None:
        '''
        Display the changes on surface.
        '''
        pygame.display.flip()

    
    def _handle_events(self) -> None:
        '''
        Takes in user's actions/inputs and respond to them.
        '''
        for event in pygame.event.get():
            self._handle_event(event)

        self._handle_keys()
        

    def _handle_event(self, event) -> None:
        '''
        Respond to certain actions such as clicking on the close button, resizing the window, etc.
        '''
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.VIDEORESIZE:
            self._create_board(event.size)
            
    
    def _handle_keys(self) -> None:
        '''
        Takes in the key inputs and utilizes the game mechanic module to make moves on board.
        '''
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            # If the user presses left arrow key, move the faller to the left by one.
            if self._fl_num < 3:
                self._state = self._new_faller.new_left(self._fl_num)
            elif self._row == 11:
                self._state = self._new_faller.left(self._row)
                self._state[9][self._new_faller.return_column()+1] = '   '
            else: 
                self._state = self._new_faller.left(self._row-1)
            self._draw_board()


        if keys[pygame.K_RIGHT]:
            # If the user presses right arrow key, move the faller to the right by one.
            if self._fl_num < 3:
                self._state = self._new_faller.new_right(self._fl_num)
            elif self._row == 11:
                self._state = self._new_faller.right(self._row)
                self._state[9][self._new_faller.return_column()-1] = '   '
            else: 
                self._state = self._new_faller.right(self._row-1)
            self._draw_board()


        if keys[pygame.K_SPACE]:
            # If the user presses space bar, rotate the faller.
            if self._fl_num < 3:
                self._state = self._new_faller.new_rotate(self._fl_num)
            elif self._row == 11:
                self._state = self._new_faller.rotate(self._row)
                self._state[self._row-2][self._new_faller.return_column()] = '   '

            else:
                self._state = self._new_faller.rotate(self._row-1)
            self._draw_board()   


        if keys[pygame.K_DOWN]:
            # If the user presses downward arrow key, move the faller down by one.
            if self._fl_num < 3:
                    if self._fl_num == 0:
                        self._new_faller.create_faller()
                    self._state = self._new_faller.new_drop(self._fl_num)
                    self._draw_board()
                    
                    self._fl_num += 1
            else: 
                if columns.Faller.not_bottom(self._state, self._row+1, self._new_faller.return_column()):
                    self._state = self._new_faller.drop(self._row)
                    self._draw_board()

                    if self._row < 11:
                        self._row += 1


if __name__ == '__main__':
    ColumnsGame().run()