class Patient:
    def __innit__ (self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

        def get_name(self):
            return self.__name

        def set_name(self, name):
            self.__name = name

        def get_bill_amount(self):
            return self.__bill_amount

        def set_bill_amount(self, bill_amount):
            self.__bill_amount = bill_amount
  
        def calculate_bill(self):
            bill = self.__bill_amount * 1
            return bill

class Senior_Patient(Patient):
    def calculate_bill(self):
        return get_bill_ammount() * 0.8

class PhilHealth_Patient(Patient):
    pass