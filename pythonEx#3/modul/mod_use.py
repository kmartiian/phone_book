import module

from module import a

# from module import*  - not recommended way to import

a=20

print(module.a)

print(a)

import module as m1

print(m1.a)

m2 = __import__('module') #str name can be generated

#reload - reload already loaded module. not save. better not to use.
