import json

obj = {1:(1,2,3), 'a': {'c':True}}
s = json.dumps(obj)
obj2 = json.loads(s)

print(obj)
print(s)
print(obj2)
