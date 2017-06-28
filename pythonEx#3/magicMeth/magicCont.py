class A:
    def __enter__(self):
        print('Enter')
        return self
    def __exit__(self, *args):
        print('Exit')

a = A()
with A() as a:
    print('In the with')
    
