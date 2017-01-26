#! python3
"""
Project:    Sandbox
Filename:   example_decorators
Created by: PJC
Created on: November 23, 2016
"""

from time import sleep
from time import time
from functools import wraps
import logging


# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def measure_time(function):
    """ Decorator that will measure the time taken to complete a functions task """
    # Allows for original function name and docstring to be maintained
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        function(*args, **kwargs)  # Allows for the passing of arguments to the function
        logger.info('{0} took: {1}'.format(function.__name__, time() - start_time))
    return wrapper


@measure_time
def wait_for(sleep_time=.01):
    """ Sleeps for a set amount of time. """
    sleep(sleep_time)


def main():
    # Decorator is run.  Functions parameters are passed to the function.
    wait_for(sleep_time=0.3)
    wait_for(0.5)
    logger.info('Function Name: {0}'.format(wait_for.__name__))
    logger.info('Doc String: {0}'.format(wait_for.__doc__))

if __name__ == '__main__':
    main()
