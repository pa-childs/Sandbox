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
    file_path = 'C:\\Work_Files\\Repositories\\sandbox\\example_files\\example_Oracle\\'
    file_name = 'config.ini'
    setup_data = {}

    try:

        with open(file_path + file_name, 'r') as file:

            configuration_info = file.readlines()

            for field in configuration_info:

                logger.debug(field.strip())

                key = re.sub('=.*$', '', field.strip())
                value = re.sub('^.*=', '', field.strip())

                setup_data[key] = value

            logger.info('Database Configuration Data Retrieved')

        return setup_data

    except IOError:

        logger.exception('Unable To Open Credential File')
        quit()


def main():

    querystring = "select * from ci_coupons order by cpn_id desc"
    column_names = []

    # Grab credentials and connection string form file
    db_connection_setup = import_setup_data()
    conn_str = u'{0}/{1}@{2}:{3}/{4}'.format(db_connection_setup['username'],
                                             db_connection_setup['password'],
                                             db_connection_setup['host'],
                                             db_connection_setup['port'],
                                             db_connection_setup['service'])

    # Setup the connection to Oracle
    oracle_connection = cx_Oracle.connect(conn_str)
    cursor = oracle_connection.cursor()
    logger.debug('DB Version: {0}\n'.format(oracle_connection.version))

    # Run the query
    cursor.execute(querystring)

    # Get the Table Description to get Column Names
    table_description = cursor.description
    logger.debug('Table Description:\n{0}\n'.format(cursor.description))

    for column in table_description:
        column_names.append(column[0])

    logger.info(column_names)

    for row in cursor:

        logger.info(row)

    oracle_connection.close()

if __name__ == '__main__':
    main()
