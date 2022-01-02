# Class variables

class Employee:
    percentage = 1.04
    def __init__(self, name, pay):    # constructor
        self.name = name
        self.pay = pay
        self.details = self.name + ' £' + str(self.pay)

    def raise_amount(self):
        self.pay = int(self.pay * Employee.percentage)


emp_1 = Employee('Maxwell', 45000)
emp_2 = Employee('Einstein', 70000)

print(emp_1.details)
print(emp_2.details)

emp_1.raise_amount()
print(emp_1.pay)
