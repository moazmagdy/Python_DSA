class employee(object):
    numemployee = 0
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.owd = 0
        employee.numemployee += 1

    def __del__(self):
        employee.numemployee -= 1
    
    def hours(self, numhours):
        self.owd += numhours * self.rate
        return "{} hours worked.".format(numhours)

    def pay(self):
        self.owd = 0
        return "Paied {}".format(self.name)

class special_employee(employee):
    def __init__(self, name, rate, bonus):
        super().__init__(name, rate)
        self.bonus = bonus

    def hours(self, numhours):
        self.owd += numhours * self.rate * self.bonus
        return "{} hours worked.".format(numhours)