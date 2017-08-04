"""
Created on May 29, 2016

@author: PJC
"""

import os
import re
import sys

class ConfigDict(dict):
    """
    Usages:
    ./assignment_4.py                           (reads out the entire config dict)
    ./assignment_4.py thiskey                   (reads out the value for 'thiskey')
    ./assignment_4.py thiskey thisvalue         (sets 'thiskey' and 'thisvalue' in the dict)

    Used to set the values in a config file.  When read from the config file the values are stored in a dictionary
    and then printed to the screen.  When written to the file, all values are written at once.  The format of the
    config file is:

    key1=value1
    key2=value2
    """
    
    def __init__(self, file_name):
        # Overrides __init__ in dict.  Opens config file, then reads the lines into the dict object.
        self._config_file = file_name
        
        if not os.path.isfile(self._config_file):

            raise IOError
            
        with open(self._config_file) as fh:
             
            lines = fh.readlines()
             
            for line in lines:
                 
                key, value = line.split('=', 1)
                value = re.sub('\n', '', value)
                dict.__setitem__(self, key, value)
    
    
    def __setitem__(self, key, value):
        # Overrides __setitem__ in dict.  Adds the new value to dict, then rights the whole dict back to the config file.
        dict.__setitem__(self, key, value)
        
        with open(self._config_file, 'w') as fh:
            
            for item in self:
                line = '{0}={1} \n'.format(item, self[item])
                fh.write(line)
                
    
    def __getitem__(self, key):
        # Overrides __getitem__ in dict. Raises KeyError in custom error class.
        if not key in self:
            
            raise ConfigKeyError(self, key)
        
        return dict.__getitem__(self, key)


class ConfigKeyError(Exception):
    """
    Setup the customer exception handling for ConfigKeyError
    """
    def __init__(self, *args):
        # Assign the exceptions arguments to their variables.
        self.keys = str(list(args[0].keys()))
        self.bad_key = args[1]
        
    
    def __str__(self):
        # Format the message for the exception.
        return 'Key "{1}" not found.  Available keys: {0}'.format(self.keys, self.bad_key)

if __name__ == '__main__':

    # Create the ConfigDict object
    cd = ConfigDict('config.txt')

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