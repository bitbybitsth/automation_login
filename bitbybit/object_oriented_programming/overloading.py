class Student:
    def __init__(self, m1, m2 , m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def __str__(self):
        return f"subject 1: {self.m1}\nsubject 2: {self.m2}\nsubject 3: {self.m3}"

    def __add__(self, other):
        return Student(self.m1+other.m1, self.m2+other.m2, self.m3+other.m3)

    def __sub__(self, other):
        pass

    def __eq__(self, other):
        if self.m1 == other.m1:
            if self.m2 == other.m2:
                if self.m3 == other.m3:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        print("Division")

    def __mod__(self, other):
        print("modulo")

    def __len__(self):
        pass

    def __repr__(self):
        pass

    def __gt__(self, other):
        pass


    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass


a = 10
b = 20
c = a+b
d = int.__add__(a, b)
#
# print("c:", c)
# print("d:", d)
#
#
s1 = Student(55,63,76)
s2 = Student(55,64,76)
# #
# s3 = s1+s2
# print(s3)
#
# s3 = s1>s2
# print(s3)
#
# s1%s2
# s1/s2

print(s1 == s2)