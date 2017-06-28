#collections incapsulation

'''
class MyList(list):
    def sum(self):
        s=0
        for i in self:
            s+=i
        return s

l = MyList([1,2,3])
print(l)
l.append(4)
print(l)
print(l.sum)
'''

class MyList:
    def __init__(self, l=[]):
        self._l = list(l)

    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)
    def add(self, value):
        self._l.append(value)
    def __setitem__(self, index, value):
        self._l[index]=value
    def __getitem__(self, index):
        if isinstance(index, tuple):
            return [self._l[i] for i in index]
        elif index == ...:
            return self._l.copy()
        else:
            return self._l[index]
    def __contains__(self, value):
        return value in self._l
    def __iter__(self):
        for i in self._l:
            yield i
'''
# this way is wrong as for i in range for j in range2 - not works
    def __iter__(self):
        print('iter')
        self._i = 0
        return(self)
    def __next__(self):
        print('next')
        if self._i == len(self._l):
            raise StopIteration
        self._i += 1
        return self._l[self._i - 1]
        
l = MyList([1,2,3])
for i in l:  #WORKS
    print(i)
for i in l:  #NOT WORKS
    for j in l:
        print(i,j)
'''


class MyListIterator:
    def __init__(self, l):
        self._l = l
        self._i = 0
    def __iter__(self):
        return self
    def __next__(self):
        
        if self._i == len(self._l):
            raise StopIteration
        self._i += 1
        return self._l[self._i - 1]

l = MyList([1,2,3])

for i in l:
    for j in l:
        print(i,j)

l = [1,2]
print(l)
l1 = MyList((l,2,3))
print(l1)
print(l1._l)

print(l[0])
print('\n')
print(dir(l1))
