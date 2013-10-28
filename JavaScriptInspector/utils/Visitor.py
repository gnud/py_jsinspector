'''
Created on Oct 27, 2013

@todo: add what type to search, e.g: function

@author: gnu_d
'''

import jsparser as jsparser
from jsparser import SyntaxError_
from collections import defaultdict
from utils import Observer

call_event = Observer.Sender()

class Visitor(object):
    CHILD_ATTRS = ['thenPart', 'elsePart', 'expression', 'body', 'initializer']

    def __init__(self, filepath):
        self.filepath = filepath
        self.functions_list = []
        
        #List of functions by line # and set of names
        self.functions = defaultdict(set)
        with open(filepath) as myFile:
            self.source = myFile.read()
    
        try:
            self.root = jsparser.parse(self.source, self.filepath)
            self.visit(self.root)
        except SyntaxError_:
            print("Syntax error in  %s" % filepath)
#         print(self.elements)
    def getFunctions(self):
        '''
        @return: list of functions
        '''
        return self.functions_list
        

    def look4Childen(self, node):
        for attr in self.CHILD_ATTRS:
            child = getattr(node, attr, None)
            if child:
                self.visit(child)
    
    def visit_NOOP(self, node):
#         print(node.type)
        pass
    
    def loop(self, node):
        name = ""
        for pnode in node:
            name+= pnode.value
        return name
    def visit_CALL(self, node):
        rules = ['bootstrap', 'jquery', 'pqgrid', 'webrtc']
        
        for r in rules:
            if r in self.filepath:
                return ''
        
        if(not "jquery" in self.filepath):
            try:
    #             print(node)
#                 print("%s|%s" %(self.filepath, node.lineno))
                name = ""
                for pnode in node:
                    name+= self.loop(pnode)
#                 print(name)
                call_event.dispatch(event='command.call', msg=name)
    #             print(dir(node[0]))
    #             exit()
            except:
                pass
        
    def visit_FUNCTION(self, node):
        # Named functions
        if node.type == "FUNCTION" and getattr(node, "name", None):
            self.functions_list.append([str(node.lineno), node.name])
            #print str(node.lineno) + " | function " + node.name #+ " | " + self.source[node.start:node.end]
#             pass
    
    
    def visit_IDENTIFIER(self, node):
        # Anonymous functions declared with var name = function() {};
        try:
            if node.type == "IDENTIFIER" and hasattr(node, "initializer") and node.initializer.type == "FUNCTION":
                self.functions_list.append([str(node.lineno), node.name])
                #print str(node.lineno) + " | function " + node.name + " | " + self.source[node.start:node.initializer.end]
                pass
        except Exception as e:
            pass
    
    def visit_PROPERTY_INIT(self, node):
    
        # Anonymous functions declared as a property of an object
        try:
            if node.type == "PROPERTY_INIT" and node[1].type == "FUNCTION":
                #print str(node.lineno) + " | function " + node[0].value + " | " + self.source[node.start:node[1].end]
                pass
        except Exception as e:
            pass
    
    
    def visit(self, root):
        call = lambda n: getattr(self, "visit_%s" % n.type, self.visit_NOOP)(n)
        call(root)
        self.look4Childen(root)
        for node in root:
            self.visit(node)