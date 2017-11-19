'''
Created on May 29, 2016

@author: PJC
'''

import os.path
import re
import sys

class ConfigDict(dict):
    '''
    Usages:
    ./assignment_3.py                           (reads out the entire config dict)
    ./assignment_3.py thiskey thisvalue         (sets 'thiskey' and 'thisvalue' in the dict)
    
    Used to set the values in a config file.  When read from the config file the values are stored in a dictionary 
    and then printed to the screen.  When written to the file, all values are written at once.  The format of the 
    config file is:
    
    key1=value1
    key2=value2
    '''
    
    def __init__(self, file_name):
        # Overrides __init__ in dict.  Opens config file, then reads the lines into the dict object.

        # Test if supplied config file exists
        if os.path.isfile(file_name):
            
            self._config_file = file_name
            
        else:
            
            print('File does not exist!')
            return
        
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
                

# Create the ConfigDict object
cd = ConfigDict('config.txt')

if len(sys.argv) == 3:
    
    # If variables supplied for new config setting add it to the file
    key = sys.argv[1]
    value = sys.argv[2]
    print('Writing Data:  {0}, {1}'.format(key, value))

    cd[key] = value

else:
    
    # Otherwise print out the current settings
    print('Reading Data')
    for key in cd.keys():
        print('   {0} = {1}'.format(key, cd[key]))
