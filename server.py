
import socket

def parse_message(decoded_message):
    """
    Takes a decoded message object, returning a parsed_message object.
    Parsed_messages hold necessary information to support print
    messages and database updates.
    """
    return -1

def print_message(parsed_message):
    """
    takes a parsed_message, returning a string representation of the 
    encoded message. Used for testing the message has been properly
    received and decoded.
    """
    return -1

def add_to_database(decoded_message):
    """
    Take a client message and call necessary SQL procedures to populate
    tables.
    """
    return -1

serverPort = 80
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")
count = 1

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    #decoded message object
    parsed_message = parse_message(message.decode())
    print("Message from: \n", clientAddress, print_message(parsed_message))

    #add to database
    add_to_database(parsed_message)
