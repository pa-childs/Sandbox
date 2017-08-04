#! python3
"""
Project:    Udemy
Filename:   section_24_network_client
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

host = 'localhost'
address = (host, 5555)
message = b"Hi, this is a test.\n"


def main():

    try:

        # Setup the network socket
        network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Set up a Internet TCP socket

        # Connect to configured address
        network_socket.connect(address)

        # Send message to address
        network_socket.sendall(message)

    except socket.errno:

        logger.error('Socket Error')

    finally:

        network_socket.close()

if __name__ == '__main__':
    main()
