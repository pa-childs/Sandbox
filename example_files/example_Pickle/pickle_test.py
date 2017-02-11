#! python3
"""
Project:    Sandbox
Filename:   openpyxl_test
Created by: PJC
Created on: June 4, 2016
"""

import pickle

# Set up two dictionary objects, obj_a will have two values added
# while obj_b will remain empty 
obj_a = {}
obj_b = {}
 
obj_a['a'] = '100'
obj_a['b'] = '200'
 
# Set up two file names to be created, one for each dictionary
file_name_a = 'obj_a.pickle'
file_name_b = 'obj_b.pickle'
 
# Create one pickle file for each object
with open(file_name_a, 'wb') as fh:
    pickle.dump(obj_a, fh)
 
with open(file_name_b, 'wb') as fh:
    pickle.dump(obj_b, fh)

# Read each pickle file and save it to a variable
with open(file_name_a, 'rb') as fh:
    test_a = pickle.load(fh)
    
with open(file_name_b, 'rb') as fh:
    test_b = pickle.load(fh)

# Print the data that was in the pickle file
print(str(test_a))
print(str(test_b))