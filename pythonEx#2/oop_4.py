#OOP4:
from classs import * # move to python dir

class A: pass

class B(A): pass

class C(A): pass

class D(B): pass

class E(B): pass

class F(D, E): pass

class G(F, C): pass



print(G.mro())
