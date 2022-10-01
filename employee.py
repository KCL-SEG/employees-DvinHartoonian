"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.totalPay = 0

    def get_pay(self):
        self.totalPay += self.salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.totalPay}."


class MonthlySalaryEmployee(Employee):
    def __init__(self, name, salary, commission = 0, commissionType = "", contracts = 0):
        super().__init__(name, salary)
        self.commission = commission
        self.commissionType = commissionType
        self.contracts = contracts

    def get_pay(self):
        super().get_pay()

        if self.commissionType == "unfixed":
            self.totalPay += self.commission * self.contracts
        elif self.commissionType == "fixed":
            self.totalPay += self.commission

        return self.totalPay

    def __str__(self):
        if not self.commissionType:
            return super().__str__()
        elif self.commissionType == "unfixed":
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.totalPay}."
        else:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}.  Their total pay is {self.totalPay}."


class HourlySalaryEmployee(Employee):
    def __init__(self, name, salary, hours, commission = 0, commissionType = "", contracts = 0):
        super().__init__(name, salary)
        self.hours = hours
        self.commission = commission
        self.commissionType = commissionType
        self.contracts = contracts

    def get_pay(self):
        super().get_pay()
        self.totalPay = self.totalPay * self.hours

        if self.commissionType == "unfixed":
            self.totalPay += self.commission * self.contracts
        elif self.commissionType == "fixed":
            self.totalPay += self.commission

        return self.totalPay

    def __str__(self):
        if not self.commissionType:
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour.  Their total pay is {self.totalPay}."
        elif self.commissionType == "unfixed":
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.totalPay}."
        else:
            return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.commission}.  Their total pay is {self.totalPay}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlySalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlySalaryEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlySalaryEmployee('Renee', 3000, 200, "unfixed", 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlySalaryEmployee('Jan', 25, 150, 220, "unfixed", 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlySalaryEmployee('Robbie', 2000, 1500, "fixed")

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlySalaryEmployee('Ariel', 30, 120, 600, "fixed")
