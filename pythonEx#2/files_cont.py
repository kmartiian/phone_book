f = open('file.txt, r+w')

f.tell() # >>> 0

# help(f.seek)

f.seek(27)
f.tell()  # 27 byte
f.write('x')
f.flush()
f.close()

obj = {1:(1,2,3), 'a': {'c':True}}
obj_str = repr(obj) # making str from {}: '{1:(1,2,3), 'a': {'c':True}}'

# pickle lib
import pickle
pickle_str = pickle.dumps(obj)  # to byte str code
obj1 = pickle.loads(pickle_str)  # back to {} 

with open('obj.pickle', 'wb') as f:
    pickle.dump(obj, f)
with open('obj.pickle', 'rb') as f:
    obj1 = pickle.load(f)

import hashlib
print(dir(hashlib))
h = hashlib.sha1()
h.update(pickle.dump(obj))
h.digest()
