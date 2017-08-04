#! python3
"""
Project:    Udemy
Filename:   section_25_network_server
Created by: PJC
Created on: September 10, 2016
"""

import logging
import socket

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

size = 512
host = ''
port = 9898


def main():

    # Setup the network socket
    network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Set up a Internet TCP socket
    network_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    network_socket.bind((host, port))  # Bind socket to host:port
    network_socket.listen(5)  # Set up to listen to up to 5 queued listeners

    # Accept transmitted data from the client
    client_connection, client_address = network_socket.accept()
    data = client_connection.recv(size)

    # If there is a data message log it to console
    if data:

        logger.info('Connection from: {0} - {1}'.format(client_address[0], data.decode('utf-8')))

    network_socket.close()

if __name__ == '__main__':
    main()
