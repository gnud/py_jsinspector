'''
Created on Oct 27, 2013

@author: gnu_d
'''

from glob import glob

from Visitor import Visitor
from Javascript import JavaScriptObj
from Scripts import Scripts

def process_script(filename):
    '''
    
    :param filename: string path to js file
    '''

    visitor = Visitor(filename)
    script = JavaScriptObj(visitor.getFunctions())
    return script

def process_files(filepath):
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
            script = process_script(filename)
#             print(script.functions_list)
            scripts.add(script)
    except Exception:
        import traceback;traceback.print_exc()

if __name__ == '__main__':
    filepath = "../data/js/"
    process_files(filepath)