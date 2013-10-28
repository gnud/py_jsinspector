'''
Created on Oct 27, 2013

@author: gnu_d
'''

import types
 
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class Sender(object):
    """
    Sender -> dispatches messages to interested callables
    """
    def __init__(self):
        self.listeners = {}
#         self.logger = logger.getLogger()
        print("constructors")
         
    def register(self,listener,events=None):
        """
        register a listener function
         
        Parameters
        -----------
        listener : external listener function
        events  : tuple or list of relevant events (default=None)
        """
        if events is not None and type(events) not in (types.TupleType,types.ListType):
            events = (events,)
              
        self.listeners[listener] = events
         
    def dispatch(self,event=None, msg=None):
#         print ("dispatching items %s" % event)
        """notify listeners """
        for listener,events in self.listeners.items():
            if events is None or event is None or event in events:
                try:
                    listener(self,event,msg)
                except (Exception,):
                    self.unregister(listener)
                    errmsg = "Exception in message dispatch: Handler '{0}' unregistered for event '{1}'  ".format(listener.func_name,event)
#                     self.logger.exception(errmsg)
             
    def unregister(self,listener):
        """ unregister listener function """
        del self.listeners[listener]   