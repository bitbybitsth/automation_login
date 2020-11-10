class SavingsAccount:

    def __init__(self, acc_no, acc_holder, acc_balance, contact_no):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.acc_balance = acc_balance
        self.contact_no = contact_no

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)


class O:
    pass

class D(O): pass

class E(O): pass

class F(O): pass

class B(D,E): pass

class C(D, F): pass

class A(B, C): pass

a = A()

# print(help(a))




