#! python3
"""
Project:    sandbox
Filename:   arrow_test.py
Created by: PJC
Created on: May 18, 2017
"""

import arrow
import colorlog
import logging

# Setup logging.  Display INFO messages and higher to console
logger = colorlog.getLogger(__name__)
logger.setLevel(colorlog.colorlog.logging.INFO)

log_handler = colorlog.StreamHandler()
log_handler.setFormatter(colorlog.ColoredFormatter('%(log_color)s%(levelname)s: %(message)s'))
log_handler.setLevel(logging.INFO)

logger.addHandler(log_handler)


def main():

    logger.info('Example of using Arrow to make datetime timezone aware.')
    logger.info('http://arrow.readthedocs.io/en/latest/\n')

    # Get times that are time zone aware in Normal and UTC formats
    local_time = arrow.now()
    utc_time = arrow.utcnow()

    # Format times as needed
    logger.info('Local Time:      {0}'.format(local_time.format('YYYY-MM-DD HH:mm:ss ZZ')))
    logger.info('UTC Time:        {0}\n'.format(utc_time.format('YYYY-MM-DD HH:mm:ss ZZ')))

    # Normal and UTC time formats can be mixed
    difference = (local_time - utc_time).total_seconds()
    logger.info('Time Difference: %.2f seconds' % difference)

    # Convert to other time zones
    local_utc_time = utc_time.to('US/Eastern')
    central_time = local_time.to('US/Central')
    logger.info('Local UTC Time:  {0}'.format(local_utc_time.format('YYYY-MM-DD HH:mm:ss ZZ')))
    logger.info('Central Time:    {0}\n'.format(central_time.format('YYYY-MM-DD HH:mm:ss ZZ')))

    # Break up Time and Date as needed
    date = local_time.date()
    time = local_time.time()
    logger.info('The Date Is {0}'.format(date))
    logger.info('The Time Is {0}'.format(time))
    logger.info('Year: {0}  Month: {1} Day: {2}'.format(local_time.year, local_time.month, local_time.day))

if __name__ == '__main__':
    main()
