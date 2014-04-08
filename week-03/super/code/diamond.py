class A(object):
    def do_your_stuff(self):
        print "doing A's stuff"
    
class B(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print "doing B's stuff"
    
class C(A):
    def do_your_stuff(self):
        A.do_your_stuff(self)
        print "doing C's stuff"
        return
    

if __name__ == '__main__':
    a = A()
    a.do_your_stuff

    b = B()
    b.do_your_stuff()

    c = C()
    c.do_your_stuff

