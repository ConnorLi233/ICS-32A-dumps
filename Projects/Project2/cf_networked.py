# cf_networked.py
#
# ICS 32A Fall 2023
# Project #2: Send Me On My Way

'''
This module contains the functions that made up the user interface
of a networked version of connectfour through the server.
'''

import cf_socket
import cf_shared
import connectfour


# These are the protected functions, it will only be used to 
# help construct other functions within the module.

def _where_to_connect() -> cf_socket.ConnectfourConncetion:
    '''
    Asks the user to specify the hostname/ip address and port number of the server,
    then start the connection. Raise an error when the connection failed.
    '''
    host = input('Enter the host (IP address or hostname): ')
    port = input('Enter the port: ')
    try:
        return cf_socket.connect(host, int(port))
    except:
        raise ConnectionError


def _get_username() -> str:
    '''
    Asks the user for the username, keep asking for a valid input if the input is invalid.
    '''
    username = input('Please enter a username: ')
    while True:
        if len(username.split()) == 1 and username.isspace() == False and username.startswith(' ') == False and username.startswith('\t') == False:
            return username
        else:
            print('Invalid')
            username = input('Please enter a username: ')


def _invalid_move(connection: cf_socket.ConnectfourConncetion, game_status: connectfour.GameState) -> connectfour.GameState:
    '''
    Keeps asking user for a valid input, when the user's first input
    was invalid and the server responded with a message 'INVALID'.
    '''
    if cf_socket.read_line(connection) == 'READY':
        while True:
            move = input('Next move: ')
            cf_socket.write_line(connection, move)
            validity = cf_socket.read_line(connection)
            if validity == 'OKAY':
                next_move = move.split()
                break
            else:
                print('Invalid move')
                cf_socket.read_line(connection)
        return cf_shared.drop_pop(game_status, next_move)

# These are the public functions, can be called when the module is imported.

def start_game(connection: cf_socket.ConnectfourConncetion, column, row) -> connectfour.GameState:
    '''
    Creates a new game board with size determined by the user input, 
    then prints the new game board with the correct format.
    '''
    cf_socket.write_line(connection, f'AI_GAME {column} {row}')
    game_status = cf_shared.start_new_game(column, row)

    return game_status


def get_validity(connection, move) -> str:
    '''
    Returns the validity message from the server: 'OKAY' or
    'INVALID', when the game has not end yet; winner when someone
    won the game.
    '''
    cf_socket.write_line(connection, move)
    validity =  cf_socket.read_line(connection)
    return validity


def user_move(connection: cf_socket.ConnectfourConncetion, move: str, game_status: connectfour.GameState, responses: tuple) -> connectfour.GameState:
    '''
    Returns the updated game board after user inputs a valid move,
    if the move is invalid, keep asking until a valid move is made.
    '''
    is_ready = responses[0]
    validity = responses[1]

    if is_ready == 'READY':
        if validity == 'OKAY' or validity == 'WINNER_RED' or validity == 'WINNER_YELLOW':
            next_move = move.split()
            game_status = cf_shared.drop_pop(game_status, next_move)
            return game_status
        else:
            print('Invalid move')
            return _invalid_move(connection, game_status)


def ai_move(connection: cf_socket.ConnectfourConncetion, game_status: connectfour.GameState) -> connectfour.GameState:
    '''
    Prints the message from the server indicating the next move, returns the updated game board 
    after the server has made a valid move. If the move was invalid, close the connection.
    '''
    move = cf_socket.read_line(connection).split()
    if cf_shared.drop_pop(game_status, move) == None:
        cf_socket.close(connection)
    else:
        print(move)
        return cf_shared.drop_pop(game_status, move)
        

def run_cf():
    '''
    Composes and outputs the user interface of the networked connectfour game
    through server: ask for host/port of the server, ask for next move,  
    print out game board, etc.
    '''
    connection = _where_to_connect()
    username = _get_username()

    cf_socket.welcome(connection, username)

    column = cf_shared.get_column()
    row = cf_shared.get_row()
    game_status = start_game(connection, column, row)

    print('Please enter your next move in the following format:')
    print('DROP/POP + Column number')
    print('Ex. DROP 5 \n')

    while True:
        ready = cf_socket.read_line(connection)
        if ready == "WINNER_YELLOW" or ready == 'WINNER_RED':
            print(ready)
            cf_socket.close(connection)
            break

        cf_shared.turn(game_status)

        while True:
            move = input('Next move: ')
            if len(move) == 0 or move.isspace() == True:
                print('Invalid input')
            elif move.split()[0] == 'DROP' or move.split()[0] == 'POP':
                responses = (ready, get_validity(connection, move))
                game_status = user_move(connection, move, game_status, responses)
                cf_shared.print_board(game_status, column, row)
                break
            else:
                print('Invalid input')

        if responses[1] == 'WINNER_RED' or responses[1] == 'WINNER_YELLOW':
            print(responses[1])
            cf_socket.close(connection)
            break

        cf_shared.turn(game_status)
        game_status = ai_move(connection, game_status)
        cf_shared.print_board(game_status, column, row)


if __name__ == '__main__':
    run_cf()