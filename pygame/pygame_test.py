#! /usr/bin/python2.7
"""
Project:    sandbox
Filename:   pygame_test
Created by: PJC
Created on: February 11, 2017
"""

import logging

# Setup logging. Display INFO message and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def main():
    # TODO: Learn some pygame
    pass


if __name__ == '__main__':
    main()
