'''
Created on Oct 27, 2013

@author: gnu_d
'''

class Scripts(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.scripts = {}
        
    def add(self, script):
        '''
        
        :param script: add Javascript object
        '''
        
        self.scripts[script.getFilename()] = script