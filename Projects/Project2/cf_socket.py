# cf_socket.py
#
# ICS 32A Fall 2023
# Project #2: Send Me On My Way

'''
This module contains functions that connect, read, write, etc., via a socket,
and communicates with the server. 
'''

from collections import namedtuple
import socket

# ConnectfourConnection is a namedtuple that stores the socket,
# along with the input/output sent via the socket.

ConnectfourConncetion = namedtuple(
    'ConnectfourConnection',
    ['socket', 'input', 'output'])

class ProtocolError:
    '''Raise an error when either side of the communication 
    did not follow the protocol.
    '''
    pass 


def connect(host: str, port: int) -> ConnectfourConncetion:  
    '''Coonect to the server, given hostname/ip address and port number.'''
    connectfour_socket = socket.socket()

    connectfour_socket.connect((host, port))

    connectfour_input = connectfour_socket.makefile('r')
    connectfour_output = connectfour_socket.makefile('w')

    return ConnectfourConncetion(connectfour_socket, connectfour_input, connectfour_output)


def close(connection: ConnectfourConncetion) -> None:
    '''Close the connectio between server and client.'''
    connection.input.close()
    connection.output.close()
    connection.socket.close()


def write_line(connection: ConnectfourConncetion, line: str) -> None:
    '''Sends a line of string to the server with End-of-line sequences'''
    connection.output.write(line + '\r\n')
    connection.output.flush()


def read_line(connection: ConnectfourConncetion) -> str:
    '''Receives a line of string from the server, as the response.'''
    return connection.input.readline()[:-1]


def welcome(connection: ConnectfourConncetion, username: str) -> bool:
    '''
    Sends 'I32CFSP_HELLO' and the username to the server, then receives
    the WELCOME message; checks if the client follows the protocol, raise an
    error if not.
    '''
    write_line(connection, f'I32CFSP_HELLO {username}')

    response = read_line(connection)

    if response == f'WELCOME {username}':
        print(response)
        return True
    else:
        close(connection)
        raise ProtocolError

    


