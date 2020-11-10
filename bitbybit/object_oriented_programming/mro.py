# C3 Algorithm is used to to resolve method resolution order.


class O: pass


class D(O): pass

class E(O): pass

class F(O): pass

class B(D, E): pass

class C(D, F): pass

class A(B, C): pass


d = A()




