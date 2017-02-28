from sys import argv
from imported import whatToImport

filename, name = argv

print 'Hello, my name is: %s, and the name of this file is: %s' % (name, filename)

print 'Hey there, I imported this: %s' % whatToImport()

print 'the name of this module is: %s' % __name__
