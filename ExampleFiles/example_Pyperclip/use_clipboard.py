#! python3
"""
Project:    Sandbox
Filename:   openpyxl_test
Created by: PJC
Created on: June 23, 2016
"""

import logging
import pyperclip

# Setup logging.  Display INFO messages and higher to console
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
logger.setLevel(logging.INFO)
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

string_one = 'This is my 1st clipboard string!'
string_two = 'This is my 2nd clipboard string!'

# Copy the string to the clipboard
pyperclip.copy(string_one)

# Paste the clipboard contents to the logging
logger.info(pyperclip.paste())

# Copy the string to the clipboard
pyperclip.copy(string_two)

# Paste the clipboard contents to the logging
logger.info(pyperclip.paste())
