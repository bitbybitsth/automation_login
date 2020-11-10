class Students:

    def __init__(self, type, value, email):
        self.first = type
        self.last_name = value
        self.email = email

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)

