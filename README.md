py_jsinspector
==============

JavaScript Inspector
- Task Plugin support for several js operations

Goal:
Find missing function calls from user code
by sepparating the js files into three groups:
a) Browser functions
This is useful if use a function which doesn't exist in some browsers
b) 3-rd party js files and caching support
Support for disabling functions check if they start with $
c) User js files from the given project
Support for disabling functions check if they start with $

