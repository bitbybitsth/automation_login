class College:

    auditorium = str()
    ground = str()

    def book_auditorioum(self):
        print(f"Auditorium booked by {self.name}")
        self.auditorium = f"booked by {self.name}"

    def book_ground(self):
        print(f"Ground booked by {self.name}")
        self.ground = True

    @property
    def is_ground_booked(self):
        if self.ground:
            return True
        else:
            return False


class EngineeringDepartment(College):

    library = str()

    def book_library(self):
        print(f"Booked by {self.name}")
        self.library = f"Booked by {self.name}"


class ITBranch(EngineeringDepartment):

    labs = str()
    def __init__(self, name):
        self.name = name


class CentalGovernmwnt:
    health_funds = 0
    security_funds = 0

    def deploy_security(self):
        pass

    def approve_funds(self):
        pass


class StateGovenrment(CentalGovernmwnt):
    def pwd(self):
        pass


class MahaNagarPalika(StateGovenrment):

     def issue_documents(self):
         pass

class NagarPalika(MahaNagarPalika):
    pass

class GramPanchyat(NagarPalika):
    pass

it_2nd = ITBranch(name="it_2nd")
it_3rd = ITBranch(name="IT_3rd")

it_2nd.book_ground()
print(it_2nd.is_ground_booked)






        