class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    def implicit(self):
        print "from child, heck yeas!"
        super(self).implicit()

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
