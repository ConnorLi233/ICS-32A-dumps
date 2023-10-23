import socket
import random

COUNTS = 'SHAKESPEARE_COUNTS'
INSULT = 'SHAKESPEARE_INSULT'
GOODBYE = 'SHAKESPEARE_GOODBYE'

def connect (host: str, port: int) -> 'connection':
    '''Connects to the Shakespeare server'''
    shaks_socket = socket.socket()
    connect_address = (host, port)
    shaks_socket.connect(connect_address)

    shaks_input = shaks_socket.makefile('r')
    shaks_output = shaks_socket.makefile('w')

    return shaks_socket, shaks_input, shaks_output

def close(connection: 'connection') -> None:
    '''Closes the connection for both sides'''
    shaks_socket, shaks_input, shaks_output = connection
    shaks_input.close()
    shaks_output.close()
    shaks_socket.close()


def send_message(connection: 'connection', message: str) -> None:
    '''Sends a message to the Shakespeare server via the connection'''
    shaks_socket, shaks_input, shaks_output = connection
    shaks_output.write(message + '\r\n')
    shaks_output.flush()


def receive_responses(connection: 'connection') -> None:
    '''Receives a response from the Shakespeare server via the connection'''
    shaks_socket, shaks_input, shaks_output = connection
    return shaks_input.readline()[:-1]


def run() -> None:
    host = 'circinus-32.ics.uci.edu'
    port = 1564

    connection = connect(host, port)
    send_message(connection, COUNTS)
    print(receive_responses(connection))

    x = random.randint(0, 50)
    y = random.randint(0, 50)
    z = random.randint(0, 50)

    send_message(connection, f'{INSULT} {x} {y} {z}')
    print(receive_responses(connection))

    send_message(connection, GOODBYE)
    print(receive_responses(connection))

    close(connection)

# Run the client only when executing the script, not when the script is imported as a modules
if __name__ == '__main__':
    run()