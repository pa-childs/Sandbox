#! python3
"""
Project:    Sandbox
Filename:   openpyxl_test
Created by: PJC
Created on: June 2, 2016
"""

import difflib

test_env_file = 'results-test_env.txt'
prod_env_file = 'results-prod_env.txt'

with open(test_env_file) as test_file:

    data1 = test_file.read()
    data1 = data1.splitlines()
    
with open(prod_env_file) as prod_file:
 
    data2 = prod_file.read()
    data2 = data2.splitlines()

# print('context_diff:') 
# for line in difflib.context_diff(data1, data2, fromfile='test_env', tofile='prod_env'):
#     print(line)
 
# print('\nndiff:') 
# diff = difflib.ndiff(data1, data2)
# print(''.join(diff))

print('\nunified_diff:')
# Adjust the n value if addition context lines are desired
for line in difflib.unified_diff(data1, data2, fromfile='test_env', tofile='prod_env', n=0):
    print(line)
