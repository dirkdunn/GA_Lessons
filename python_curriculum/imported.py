def whatToImport():
    return 'I return a string! %s' % __name__

class imAModule(object):
    def __init__(self):
        self.hello = self.helloWorld()

    def helloWorld(self):
        return 'hello, world! from %s' % __name__
