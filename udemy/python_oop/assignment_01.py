'''
Created on May 21, 2016

@author: PJC
'''

class MaxSizeList(object):
    '''
    Create a simple class, MaxSizeList, that acts a little bit like a list, with a pre-configured limit on its size.  
    '''
    def __init__(self, value):
        # Set Instance Attributes
        self.my_list = []
        self.max_size = value
    
    def push(self, element):
        # Method to append element to list and maintain list size
        self.my_list.append(element)
        list_len = len(self.my_list)
        
        if list_len > self.max_size:
            
            self.my_list.pop(0)
    
    def get_list(self):
        # Method to return current list
        return self.my_list

# Create two List MaxSizeList instances with different Max_Sizes
# Add Elements to each list and then print the lists to see what 
# they contain

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())