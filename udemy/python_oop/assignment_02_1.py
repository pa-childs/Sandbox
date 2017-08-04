'''
Created on May 22, 2016

@author: PJC
'''

import abc
import datetime


class WriteFile(object):
    '''
    The parent class to two classes; LogFile and DelimFile.  It does work that is common between them.   Not intended to be instantiated.  
    '''
    __metaclass__ = abc.ABCMeta
        
    @abc.abstractmethod
    def write(self, string):
        return
    
    def __init__(self, filename):
        self.file_name = filename
        
    def write_string(self, string):
        # Open file, write a string to it, and close the file
        fh = open(self.file_name, 'a')
        fh.write(string + '\n')
        fh.close

class LogFile(WriteFile):
    '''
    This instance writes a date and message to a log file.  
    '''  
    def write(self, string):
        # Take the input string and format it for writing to the log
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        
        string = str(dt_str) + '  ' + string
        
        self.write_string(string)
    

class DelimFile(WriteFile):
    '''
    This instance writes values separated by a delimiter.  
    '''    
    def __init__(self, filename, delimiter):
        super(DelimFile, self).__init__(filename)
        self.delim = delimiter
     
    def write(self, element_list):
        # Take the input list, join the elements into a string that is
        # delimited by the delimiter, and write the string to a file
        string = self.delim.join(element_list)
        
        self.write_string(string)


# Test code that will generate expected output. Create one object for
# each test class.  Then write two lines to each file.
log = LogFile('log.txt')                  
mydelim = DelimFile('data.csv', ',')      

log.write('this is a log message')        
log.write('this is another log message')  

mydelim.write(['a', 'b', 'c', 'd'])       
mydelim.write(['1', '2', '3', '4'])      

# # Expected Output 
# # text of log.txt
# 2015-01-21 18:35   this is a log message
# 2015-01-21 18:35   this is another log message
# 
# # text of data.csv
# a,b,c,d
# 1,2,3,4
