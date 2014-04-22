import pickle 

from badpicklemodule import foo


x = foo()

print x()

print pickle.dumps(x)
