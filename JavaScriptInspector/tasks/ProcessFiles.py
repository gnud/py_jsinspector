'''
Created on Oct 28, 2013

@author: gnu_d
'''

from glob import glob

from utils.Visitor import Visitor
from utils.Javascript import JavaScriptObj
from utils.Scripts import Scripts

name = "Process Files"
details = "Process javascripts directory"
argument_type = "dirselect"

class ProcessFiles(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def process_script(self, filename):
        '''
        
        :param filename: string path to js file
        '''
    
        visitor = Visitor(filename)
        script = JavaScriptObj(visitor.getFunctions())
        return script
    
    def task(self, filepath):
        '''
        Process a given filepath
        :param filepath:string to directory containing js files
        or a js file
        '''
    
        try:
            js_files = glob(filepath+"/*.js")
            print(js_files)
            scripts = Scripts()
            
            for filename in js_files:
                script = self.process_script(filename)
    #             print(script.functions_list)
                scripts.add(script)
        except Exception:
            import traceback;traceback.print_exc()