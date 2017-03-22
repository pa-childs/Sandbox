#! python3
"""
Project:    Sandbox
Filename:   example_lambda
Created by: PJC
Created on: November 18, 2016
"""

import logging

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def main():
    squares = list(map(lambda number: number**2, range(10)))
    logger.info('Squares: {0}'.format(str(squares)))

    titles = list(map(lambda name: name.title(), ('the hobbit', 'the expanse', 'the avengers')))
    logger.info('Titles: {0}'.format(str(titles)))

    result = lambda number: number ** 2
    logger.info('Sum: {0}'.format(str(result(5))))

if __name__ == '__main__':
    main()
