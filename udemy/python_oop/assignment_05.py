'''
Created on June 4, 2016

@author: PJC
'''

import os
import pickle
import sys

class ConfigDict(dict):
    '''
    Usages:
    ./assignment_5.py                           (reads out the entire config dict)
    ./assignment_5.py thiskey                   (reads out the value for 'thiskey')
    ./assignment_5.py thiskey thisvalue         (sets 'thiskey' and 'thisvalue' in the dict)
    
    Used to set the values in a pickle file.  When read from the pickle file the values are stored in a dictionary 
    and then printed to the screen.  When written to the file, all values are written at once.  The pickle file 
    contains the stored ConfigDict.
    '''
    
    def __init__(self, file_name):
        # Overrides __init__ in dict.  Opens pickle file, then reads the lines into the dict object.
        self._config_file = file_name
        
        if not os.path.isfile(self._config_file):
                
            with open(self._config_file, 'w') as fh:
                    
                pickle.dump({}, fh)

        
        with open(self._config_file) as fh:
             
            loaded_dict = pickle.load(fh)
            self.update(loaded_dict)
        
    
    def __setitem__(self, key, value):
        # Overrides __setitem__ in dict.  Adds the new value to dict, then rights the whole dict back to the pickle file.
        dict.__setitem__(self, key, value)
        
        with open(self._config_file, 'w') as fh:
            
            pickle.dump(self, fh)
                
    
    def __getitem__(self, key):
        # Overrides __getitem__ in dict. Raises KeyError in custom error class.
        if not key in self:
            
            raise ConfigKeyError(self, key)
        
        return dict.__getitem__(self, key)


class ConfigKeyError(Exception):
    '''
    Setup the customer exception handling for ConfigKeyError
    '''
    def __init__(self, *args):
        # Assign the exceptions arguments to their variables.
        self.keys = str(list(args[0].keys()))
        self.bad_key = args[1]
        
    
    def __str__(self):
        # Format the message for the exception.
        return 'Key "{1}" not found.  Available keys: {0}'.format(self.keys, self.bad_key)


# Create the ConfigDict object
cd = ConfigDict('config.pickle')

# if 2 arguments on the command line,
# set a key and value in the object's dictionary
if len(sys.argv) == 3:
    
    key = sys.argv[1]
    value = sys.argv[2]
    print('Writing data:  {0}, {1}'.format(key, value))
    cd[key] = value

# if 1 argument on the command line, treat it as a key and show the value
elif len(sys.argv) == 2:
    
    print('Reading a value')
    key = sys.argv[1]
    print('The value for {0} is {1}'.format(sys.argv[1], cd[key]))

# if no arguments on the command line, show all keys and values
else:
    
    print('Keys/Values:')
    for key in cd.keys():
        
        print('   {0} = {1}'.format(key, cd[key]))

