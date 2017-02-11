#! python3
"""
Project:    Sandbox
Filename:   example_generators
Created by: PJC
Created on: November 21, 2016
"""

import logging

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def get_squares_gen(number_range):
    """ Generator used to supply squares of a range of numbers """
    for number in range(number_range):

        yield number ** 2


def geometric_progression(number_1, number_2):
    """ Generator that contains Return once condition is met """
    exponent = 0
    while True:

        result = number_1 * number_2 ** exponent
        if result <= 100000:

            yield result

        else:

            return

        exponent += 1


def counter(start=0):
    """ Generator that changes behavior via Send method"""
    n = start
    while True:

        result = yield n
        print(type(result), result)
        if result == 'Q':

            break

        n += 1


def main():
    # Uses get_squares_gen generator
    logger.info("Generator Creates: {0}\n".format(list(get_squares_gen(10))))

    logger.info("Generator Creates: {0}".format(list(get_squares_gen(4))))
    squares = get_squares_gen(4)

    try:

        logger.info(next(squares))
        logger.info(next(squares))
        logger.info(next(squares))
        logger.info(next(squares))
        logger.info(next(squares))

    except StopIteration:

        logger.info('There Are No More Results\n')

    # Uses geometric_progression generator
    logger.info('Generator Shows Geometric Progression')
    for result in geometric_progression(2, 5):

        logger.info(result)

    logger.info('Progression Ends\n')

    # Uses counter generator
    logger.info('Change Generator Behavior Via Send Method')
    count = counter()

    try:

        logger.info(next(count))
        logger.info(next(count))
        logger.info(next(count))
        logger.info(count.send('Q'))

    except StopIteration:

        logger.info('Iteration Has Stopped\n')

if __name__ == '__main__':
    main()
