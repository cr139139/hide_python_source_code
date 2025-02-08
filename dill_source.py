# Do not try to look for the source code! It is being tracked.
import dill
import numpy as np

class MyClass:
    def __init__(self, x, y):
        self.np = np
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def np_zero(self):
        return self.np.zeros(1)


# Pickle the object
with open('my_object.pkl', 'wb') as f:
    # pickle.dump(MyClass, f)
    dill.dump(MyClass, f, fmode=dill.CONTENTS_FMODE)

# Unpickle the object
with open('my_object.pkl', 'rb') as f:
    loaded_class = dill.load(f)

    dill.detect.trace(True)
    dill.pickles(loaded_class)
    print(dill.source.getsource(dill.detect.code(loaded_class.add)))
    print(dill.source.getsource(dill.detect.code(loaded_class.np_zero)))

obj = loaded_class([10], [20])
print(obj.x)
print(obj.y)
print(obj.add())
print(obj.np_zero())
