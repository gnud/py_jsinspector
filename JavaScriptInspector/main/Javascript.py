'''
Created on Oct 27, 2013

@author: gnu_d
'''

class JavaScriptObj(object):
    '''
    classdocs
    '''


    def __init__(self, functions_list):
        '''
        Constructor
        '''
        
        # Dictionary with functions, key is set by the name of the function
        # value is the linenumber
        self.functions_list = {}
        for f in functions_list:
            self.functions_list[f[1]] = f[0]
        
    def getFilename(self):
        '''
        Returns the filename
        '''
        
    def find_function(self, fname):
        '''
        Searches for a function
        :param fname: String name of the function
        '''
        
        if self.functions_list.has_key(fname):
            return True
        
        return False
    
    def get_functions(self):
        '''
        Retrieves all the functions
        '''
        
        return self.functions_list
        