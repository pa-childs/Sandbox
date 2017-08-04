'''
Created on May 22, 2016

@author: PJC
'''
import datetime

class WriteFile(object):
    '''
    This writes a string to a file based on the format object that is supplied.
    '''    
    def __init__(self, filename, writer):
        self.file_name = filename
        self.formatter = writer()
        
    def write(self, string):
        # Open file, write formatted string to it, and close the file
        self.fh = open(self.file_name, 'a')
        self.fh.write(self.formatter.format(string) + '\n')
        self.fh.close()


class LogFileFormat(object):
    '''
    This formats a date and message string.  
    '''  
    def format(self, string):
        # Format the string for the log file
        dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        string = str(dt_str) + '  ' + string
        
        return string
    

class DelimFileFormat(object):
    '''
    This formats list values separated by a delimiter into a string. 
    '''    
    def __init__(self):
        self.delim = ','
     
    def format(self, element_list):
        # Format the element_list for the csv file
        string = self.delim.join(element_list)
        
        return string


# Test code that will generate expected output. Create one object for
# each test class.  Then write two lines to each file.
wf1 = WriteFile('log.txt', LogFileFormat)                  
wf2 = WriteFile('data.csv', DelimFileFormat)      

wf1.write('this is a log message')        
wf1.write('this is another log message')  

wf2.write(['a', 'b', 'c', 'd'])       
wf2.write(['1', '2', '3', '4'])      

# # Expected Output 
# # text of log.txt
# 2015-01-21 18:35   this is a log message
# 2015-01-21 18:35   this is another log message
# 
# # text of data.csv
# a,b,c,d
# 1,2,3,4
