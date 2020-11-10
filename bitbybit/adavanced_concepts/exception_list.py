class MedicineExpired(Exception):

    def __init__(self, msg, name, date):
        self.msg = msg
        self.medicine_name = name
        self.expired_date = date

