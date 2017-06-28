#OOP5
from classs import * # ????


class A:
    def __init__(self):
        print("A")
        super.__init__()

class B(A):
    def __init__(self):
        print("B")
        super.__init__()

class C(A):
    def __init__(self):
        print("C")
        super.__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super.__init__()

class E:
    def __init__(self):
        print("E")
        super.__init__()

class F(E, A):
    def __init__(self):
        print("F")
        super.__init__()

class G:
    def __init__(self):
        print("G")
        super.__init__()

class J(A, G):
    def __init__(self):
        print("J")
        super.__init__()


