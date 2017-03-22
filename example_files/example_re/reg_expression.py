#! python3
"""
Project:    Sandbox
Filename:   reg_expression
Created by: PJC
Created on: September 15, 2016
"""

import logging
import re

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)


def regex_found(match_object):

    if match_object is None:

        return False

    return True


def main():

    search_pattern = 'RegEx'
    string1 = 'RegEx is the term to be matched'
    string2 = 'Looking for a RegEx term'
    string3 = 'Not trying to match anything'

    # TODO: match
    # Setup a reusable pattern for matching.  The search_pattern must be at start of the string.
    logger.info('Doing RegEx Matches...')

    # pattern = re.compile(search_pattern)
    # match_result = pattern.match(string1)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string1))
    # logger.info('Matched = {0}'.format(regex_found(match_result)))
    #
    # match_result = pattern.match(string2)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string2))
    # logger.info('Matched = {0}'.format(regex_found(match_result)))
    #
    # match_result = pattern.match(string3)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string3))
    # logger.info('Matched = {0}\n'.format(regex_found(match_result)))

    # Directly perform matching, not reusable
    # match_result = re.match(search_pattern, string1)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string1))
    # logger.info('Matched = {0}'.format(regex_found(match_result)))
    #
    # match_result = re.match(search_pattern, string2)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string2))
    # logger.info('Matched = {0}'.format(regex_found(match_result)))
    #
    # match_result = re.match(search_pattern, string3)
    # logger.info('Searching for "{0}" in the string "{1}"\n'.format(search_pattern, string3))
    # logger.info('Matched = {0}'.format(regex_found(match_result)))

    # TODO: search
    # Setup a reusable pattern for searching.  The search_pattern can be anywhere in the string.
    logger.info('Doing RegEx Searches...')

    pattern = re.compile(search_pattern)
    # search_result = pattern.search(string1)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string1))
    # logger.info('Matched = {0}'.format(regex_found(search_result)))
    #
    # search_result = pattern.search(string2)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string2))
    # logger.info('Matched = {0}'.format(regex_found(search_result)))
    #
    # search_result = pattern.search(string3)
    # logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string3))
    # logger.info('Matched = {0}\n'.format(regex_found(search_result)))

    # Directly perform searching, not reusable
    search_result = re.search(search_pattern, string1)
    logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string1))
    logger.info('Matched = {0}'.format(regex_found(search_result)))

    search_result = re.search(search_pattern, string2)
    logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string2))
    logger.info('Matched = {0}'.format(regex_found(search_result)))

    search_result = re.search(search_pattern, string3)
    logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string3))
    logger.info('Matched = {0}\n'.format(regex_found(search_result)))

    # TODO: findall
    # Setup a reusable pattern for searching.  All instance of the search_pattern will be found in the string.
    logger.info('Doing RegEx Findall Search...')

    search_pattern = '[T|t]o'
    string4 = 'To be or not to be...'

    pattern = re.compile(search_pattern)
    search_result = pattern.findall(string4)
    logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string4))
    logger.info('Results = {0}'.format(search_result))

    # Empty matches are a part of the result for findall
    search_pattern = r'a*'
    string5 = 'abacadabra'

    pattern = re.compile(search_pattern)
    search_result = pattern.findall(string5)
    logger.info('Searching for "{0}" in the string "{1}"'.format(search_pattern, string5))
    logger.info('Results = {0}\n'.format(search_result))

    # TODO: finditer
    # Setup a reusable pattern for searching.  Multiple match objects are created and iterated through.
    logger.info('Doing RegEx Finditer Search...')

    search_pattern = r'(\w+) (\w+)'
    string6 = 'one two three four'
    count = 1

    pattern = re.compile(search_pattern)
    match_objects = pattern.finditer(string6)

    for match_object in match_objects:

        logger.info('Match {0}: {1}'.format(count, match_object.groups()))
        count += 1

    logger.info('\n')

    # TODO: split
    # Setup a reusable pattern for searching.  Split strings with a RegEx.
    logger.info('Doing RegEx Split of String...')

    search_pattern = r'\W'  # Opposite of words i.e. whitespace

    pattern = re.compile(search_pattern)
    split_result = pattern.split(string6)
    logger.info('Splitting on "{0}" in the string "{1}"'.format(search_pattern, string6))
    logger.info('Results = {0}\n'.format(split_result))

    # Setup a reusable pattern for searching.  Split strings with a RegEx.  Include matched pattern in result.
    search_pattern = r'(-)'
    string7 = '734-555-1234'

    pattern = re.compile(search_pattern)
    split_result = pattern.split(string7)
    logger.info('Splitting on "{0}" in the string "{1}"'.format(search_pattern, string7))
    logger.info('Results = {0}\n'.format(split_result))

    # TODO: sub
    # Setup a reusable pattern for searching. Substitute the pattern for a word in the string.
    logger.info('Doing Regex Substitution...')

    search_pattern = r'blue'
    substitute_word = 'grey'
    string8 = 'The sky is blue'

    pattern = re.compile(search_pattern)
    substitution_result = pattern.sub(substitute_word, string8)
    logger.info('Substituting  "{0}" for "{1}" in the string "{2}"'.format(search_pattern, substitute_word, string8))
    logger.info('Results = {0}\n'.format(substitution_result))

    search_pattern = r'\*(.*?)\*'
    string9 = 'Title: *The Hobbit* By: *J.R.R. Tolkien*'

    pattern = re.compile(search_pattern)
    substitution_result = pattern.sub(r'<b>\g<1><\\b>', string9)
    logger.info('Substituting  bold tags for each asterisk in the string "{2}"'.format(search_pattern, substitute_word, string9))
    logger.info('Results = {0}\n'.format(substitution_result))

    # TODO: subn
    # Setup a reusable pattern for searching. Substitute the pattern for a word in the string. Note the number
    # of changes that are made.

    search_pattern = r'\*(.*?)\*'

    pattern = re.compile(search_pattern)
    substitution_result = pattern.subn(r'<b>\g<1><\\b>', string9)
    logger.info('Substituting  bold tags for each asterisk in the string "{2}"'.format(search_pattern, substitute_word, string9))
    logger.info('Results = {0}\n'.format(substitution_result))

    # TODO: Grouping - Backreferences
    # Setup a reusable pattern for searching. Swap substrings based on grouping
    string_id = r'1-a\n20-baer\n34-afcr'
    search_pattern = r'(\d+)-(\w+)'

    pattern = re.compile(search_pattern)
    result = pattern.sub(r'\2-\1', string_id)
    logger.info('Swapping substrings in {0}'.format(string_id))
    logger.info('New String = {0}\n'.format(result))

    # TODO: Grouping - Named Groups
    # Setup a reusable pattern for searching. Break substring into named grouping
    string = r'Hello World'
    search_pattern = r'(?P<first>\w+) (?P<second>\w+)'

    pattern = re.compile(search_pattern)
    match = re.search(pattern, string)

    logger.info('Splitting string into groups: {0}'.format(string))
    logger.info('First Group: {0}'.format(match.group('first')))
    logger.info('Second Group: {0}\n'.format(match.group('second')))

    # Setup a reusable pattern for searching. Swap substrings based on named grouping
    string = r'1-a\n20-baer\n34-afcr'
    search_pattern = r'(?P<country>\d+)-(?P<id>\w+)'

    pattern = re.compile(search_pattern)
    result = pattern.sub(r'\g<id>-\g<country>', string)
    logger.info('Swapping substrings in {0}'.format(string))
    logger.info('New String = {0}\n'.format(result))

    # TODO: Grouping - Non-Capturing Groups
    # Setup a reusable pattern for searching. Determine if a patterns group is contained in string.
    string = r'Batman'
    search_pattern = r'(?:Bat|Super)man'

    pattern = re.compile(search_pattern)

    try:

        match = re.search(pattern, string).groups()
        logger.info('Match Found In String')
        logger.info('String: {0}\nPattern: {1}'.format(string, search_pattern))
        logger.info('Group Not Captured: {0}\n'.format(match))

    except AttributeError:

        logger.info('Match Not Found In String')
        logger.info('String: {0}\nPattern: {1}\n'.format(string, search_pattern))

    # TODO: Grouping - Special Cases


    # TODO: Grouping - Overlapping Groups



if __name__ == '__main__':
    main()
