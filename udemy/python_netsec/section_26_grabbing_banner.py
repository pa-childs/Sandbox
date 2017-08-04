#! python3
"""
Project:    Udemy
Filename:   section_26_grabbing_banner
Created by: PJC
Created on: September 10, 2016
"""

import logging
import re
import socket

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

address = 'www.amazon.com'
http_get = b'GET / HTTP/1.1\nHost: www.amazon.com\n\n'
data = ''


def main():

    try:

        logger.info('Opening Connection To: {0}'.format(address))
        network_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        network_socket.connect((address, 80))

        network_socket.sendall(http_get)
        returned_data = network_socket.recvfrom(1024)

    except socket.error:

        logger.error('Socket Error: {0}'.format(socket.errno))
        quit()

    finally:

        logger.info('Closing Connection')
        network_socket.close()

    string_data = returned_data[0].decode('utf-8')
    html = string_data.splitlines()

    # Find server type in returned string data
    for line in html:

        if re.search('Server:', line):

            logger.info(line)

if __name__ == '__main__':
    main()
