import dill
import numpy as np

# Unpickle the object
with open('my_object.pkl', 'rb') as f:
    loaded_class = dill.load(f)

    try:
        dill.detect.trace(True)
        dill.pickles(loaded_class)
        print(dill.source.getsource(dill.detect.code(loaded_class.add)))
        print(dill.source.getsource(dill.detect.code(loaded_class.np_zero)))
    except:
        print("cannot reach the source code!")

obj = loaded_class([10], [20])
print(obj.x)
print(obj.y)
print(obj.add())
print(obj.np_zero())