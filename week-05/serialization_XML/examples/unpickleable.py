import pickle 

from badpicklemodule import foo

def foo2():
    return 1

x = foo()

print x()

print "foo2: " + pickle.dumps(foo2)
print "x: " + pickle.dumps(x)
