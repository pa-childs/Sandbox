#! python3
"""
Project:    Sandbox
Filename:   openpyxl_test
Created by: PJC
Created on: June 15, 2016
"""

import logging
import pymysql.cursors
import random

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Connect to the database
try:

    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='subscriptions_production',
                                 port=3306)

    logger.info('Connection Created')

except Exception as e:

    logger.exception('Connection Failed')
    logger.exception(e)

try:

    # Insert a record to the Test_Queue table
    with connection.cursor() as cursor:

        prd_id = random.randrange(10000, 50000)

        logger.info('Inserting prd_id: {0}'.format(prd_id))
        sql = "insert into subscriptions_production.test_queue (prd_id) values (%s)"
        cursor.execute(sql, prd_id)

        connection.commit()
        logger.info('Insert Succeeded')

    # Retrieve the inserted record from the Test_Queue table
    with connection.cursor() as cursor:

        logger.info('Retrieving prd_id: {0}'.format(prd_id))
        sql = "select id, prd_id from subscriptions_production.test_queue where prd_id = %s"
        cursor.execute(sql, prd_id)
        result = cursor.fetchone()

        logger.info('Record Set Retrieved')
        logger.info(result)

except Exception as e:

    logger.exception('Data Manipulation Failed')
    logger.exception(e)

finally:

    connection.close()
    logger.info('Connection Closed')


print('test')
for x in range(1,11):
    print('More Testing...')
