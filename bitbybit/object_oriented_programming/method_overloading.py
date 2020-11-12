class Student:

    def engg_addmission(self, phy, math, chem = None, bio = None):
        print("you have granted admission to engineering")

    def __init__(self, phy, math = None, chem = None, bio = None):
        self.phy = phy
        if math:
            self.math = math
        if chem:
            self.chem = chem
        if bio:
            self.bio = bio

    def __str__(self):
        return f"{self.__dict__}"

"""""

this is an urgent work

"""





S1 = Student(phy=55, math=67, chem=56)
s2 = Student(phy=45, bio=55)

print(S1)
print(s2)

S1.engg_addmission(phy=55, math=55)
s2.engg_addmission(phy=56, math=56, chem=56)
s2.engg_addmission(55,67,45,44)