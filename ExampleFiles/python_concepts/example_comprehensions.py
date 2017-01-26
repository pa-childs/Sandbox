#! python3
"""
Project:    Sandbox
Filename:   example_comprehensions
Created by: PJC
Created on: November 18, 2016
"""

from string import ascii_lowercase
import logging

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def main():
    # Basic List Comprehension
    squared = [n **2 for n in range(10)]
    logger.info('Squared: {0}'.format(str(squared)))

    even_squared = [number ** 2 for number in range(10) if not number % 2]
    logger.info('Even Squared: {0}'.format(str(even_squared)))

    # Nested List Comprehension
    points = '1234'
    coordinates = [(points[a], points[b]) for a in range(len(points)) for b in range(a, len(points))]
    logger.info('Distinct Coordinates: {0}\n'.format(str(coordinates)))

    # Basic Dict Comprehension
    logger.info('ascii_lowercase: {0}'.format(str(ascii_lowercase)))

    letter_map = {letter: number for number, letter in enumerate(ascii_lowercase, 1)}
    logger.info('Letter Map: {0}\n'.format(str(letter_map)))

    # Basic Set Comprehension
    word = 'sesquipedalian'
    letters = set(c for c in word)
    logger.info('Letters: {0}'.format(str(letters)))

if __name__ == '__main__':
    main()
