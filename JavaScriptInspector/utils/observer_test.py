'''
Created on Oct 27, 2013

@author: gnu_d
'''
from Observer import Sender

class ExampleListener(object):
    def __init__(self,name=None):
        self.name = name
     
    def method(self,sender,event,msg=None):
        print "[{0}] got event {1} with message {2}".format(self.name,event,msg)
                    
if __name__=="__main__":
    print 'demonstrating event system'
     
     
    call_event = Sender()
    call_event1 = Sender()
    bob = ExampleListener('bob')
    charlie = ExampleListener('charlie')
    dave = ExampleListener('dave')
     
     
    # add subscribers to messages from alice
    call_event.register(bob.method,events='call') # listen to 'event1'
    call_event.register(charlie.method,events ='call') # listen to 'event2'
#     call_event.register(dave.method) # listen to all events
     
    # dispatch some events
    call_event.dispatch(event='call')
    call_event.dispatch(event='call',msg=[1,2,3])
#     alice.dispatch(msg='attention to all')
     
    print 'Done.'