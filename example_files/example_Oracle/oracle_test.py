#! python3
"""
Project:    sandbox
Filename:   oracle_test.py
Created by: PJC
Created on: March 20, 2017
"""

import cx_Oracle
import logging
import re

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def import_setup_data():
    """
    Grab the credentials and database connection strings from a file.

    :rtype: list
    :return: Returns a list with the username, password, host, port, and service.  On failure the test is aborted.
    """

    logger.debug('\nimport_credentials')

    file_path = 'C:\\Work_Files\\Repositories\\sandbox\\ExampleFiles\\example_Oracle\\'
    file_name = 'config.ini'
    setup_data = {}

    try:

        with open(file_path + file_name, 'r') as file:

            configuration_info = file.readlines()

            for field in configuration_info:

                logger.info(field)

                key = re.sub('=.*$', '', field.strip())
                value = re.sub('^.*=', '', field.strip())

                setup_data[key] = value

            logger.info('Database Configuration Data Retrieved')

        return setup_data

    except IOError:

        logger.exception('Unable To Open Credential File')
        quit()


def main():

    db_connection_setup = import_setup_data()

    conn_str = u'{0}/{1}@{2}:{3}/{4}'.format(db_connection_setup['username'],
                                             db_connection_setup['password'],
                                             db_connection_setup['host'],
                                             db_connection_setup['port'],
                                             db_connection_setup['service'])

    oracle_connection = cx_Oracle.connect(conn_str)
    logger.info('DB Version: {0}'.format(oracle_connection.version))

    cursor = oracle_connection.cursor()
    querystring = "select * from ci_coupons"
    cursor.execute(querystring)

    for row in cursor:
        logger.info(row)

    oracle_connection.close()

if __name__ == '__main__':
    main()
