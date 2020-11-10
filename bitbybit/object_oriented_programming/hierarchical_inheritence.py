class A:
    def display(self):
        print("Printing from A")


class B(A):

    def display(self):
        print("Printing from B")


class C(A):
    pass
    # def display(self):
    #     print("Printing from C")


class D(B):
    pass
    # def display(self):
    #     print("Printing from D")

class E(B):

    def display(self):
        print("Printing from E")


class F(C):
    pass
    # def display(self):
    #     print("Printing from A")

class K:
     def display(self):
         print("Printing from K")


class G(K, C):
   pass



g = G()
g.display()
print(help(g))




