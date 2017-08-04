#! python3
"""
Project:    Udemy
Filename:   section_27_http_request
Created by: PJC
Created on: September 10, 2016
"""

import http.client
import logging

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

website = 'www.infiniteskills.com'


def main():

    logger.info('Making HTTP Request to: {0}\n'.format(website))

    # Setup the HTTP connection
    http_connection = http.client.HTTPConnection(website)

    # Make request to server
    http_connection.request('GET', '/')

    # Retrieve response from server
    http_response = http_connection.getresponse()

    logger.info('Status Code: {0}\n'.format(http_response.code))
    logger.info('HTTP Headers: \n{0}\n'.format(http_response.headers))

    logger.info('HTML: \n')
    html_text = http_response.readlines()

    for line in html_text:

        # Convert byte array into utf-8 and display to console
        logger.info(line.decode('utf-8'))

if __name__ == '__main__':
    main()
