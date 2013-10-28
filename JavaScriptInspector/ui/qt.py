'''
Created on Oct 28, 2013

@author: gnu_d
'''

import sys
from PyQt4 import QtCore, QtGui, uic, Qt
from tasks.ProcessFiles import ProcessFiles
import threading
from utils import Observer
from threading import Event

call_event = Observer.Sender()


class Worker(QtCore.QThread):

    def __init__(self, method, arguments, parent=None):
        super(Worker, self).__init__(parent)
        self.__quitting = Event()
        self.method = method
        self.arguments = arguments

    def run(self):
        self.method(self.arguments)

class ExampleListener(object):
    def __init__(self, parent=None, name=None):
        self.name = name
        self.parent = parent
     
    def method(self, sender, event, msg=None):
        print "[{0}] got event {1} with message {2}".format(self.name, event, msg)
        if self.parent != None:
            self.parent.ui.calls_list.addItem(msg)

class UIWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # Set up the user interface from Designer.
        self.ui = uic.loadUi("../data/ui/qt.ui")
        self.ui.show()
        self.call_listener = ExampleListener(name='gui', parent=self)
        
        self.fillTaskList()
        
        QtCore.QObject.connect(self.ui.command_list, QtCore.SIGNAL('changed()'), self.onCommandChanged)
        QtCore.QObject.connect(self.ui.cmd_exec, QtCore.SIGNAL('clicked()'), self.runTask)
        
        call_event.register(self.call_listener.method, events='command.call')
    def onCommandChanged(self):
        print("callback running")
    
    def fillTaskList(self):
        import pkgutil
        import tasks
        package = tasks
        prefix = package.__name__ + "."
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            print "Found submodule %s (is a package: %s)" % (modname, ispkg)
#             module = __import__(modname, fromlist="dummy")
            print "Imported", modname
            task_name = modname.split(".")[1]
            fullname = "%s" %(task_name)
            m = __import__ (modname)
            print(dir(m))
            print(sys.getrefcount(m))
            name = getattr(m, fullname)
            print(sys.getrefcount(m))
            print(name.name[:])
            print(name.details[:])
            print(sys.getrefcount(m))
            self.ui.command_list.addItem(modname, userData=name)

    def runTask(self):
        '''
        TODO: generate an UI form for the arguments type, e.g: directory chooser, file choose, etc ...
        based on the task argument_type, for now just a text field 
        :param task_name:
        '''
        print(self.ui.command_list.currentText())
        print(self.ui.cmd_args.text())
        
        cmd = self.ui.command_list.currentText()
        self.worker = Worker(cmd.task, self.ui.cmd_args.text(), parent=self)
        self.worker.start()


def main():
    app = QtGui.QApplication(sys.argv)
    window = UIWindow()
    sys.exit(app.exec_())
