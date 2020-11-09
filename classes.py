class Employee:

    amount_Inc = 1.04

    def __init__(self, first_Name, last_Name, pay):
        self.first_Name = first_Name
        self.last_Name = last_Name
        self.email = f"{first_Name}.{last_Name}@example.com"
        self.pay = pay

    def fullName(self):
        return f"{self.first_Name} {self.last_Name}"

    def apply_Increment(self):
        self.pay = int(float(self.pay) * self.amount_Inc)

class Dev(Employee):
    amount_Inc = 1.01
    def __init__(self, fname, lname, pro_lang, pay):
        Employee.__init__(self, fname, lname, pay)
        self.pro_lang = pro_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, Employees = None):
        super().__init__(fname, lname, pay)
        if Employees is None:
            Employees = []
        else:
            self.Employees = Employees

    def addEmp(self, emp):
        if emp not in self.Employees:
            self.Employees.append(emp)

    def removeEmp(self, emp):
        if emp in self.Employees:
            self.Employees.remove(emp)

    def printEmps(self):
        for emp in self.Employees:
            print("Employee: ", emp.fullName())

developer_1 = Dev('Anderson', 'Michael', 'Php', 9000)
developer_2 = Dev('Test', 'Subject', 'Alpha', 1)

mg_1 = Manager('John', 'Doe', 91111, [developer_1])

print(mg_1.email)
mg_1.addEmp(developer_1)

mg_1.addEmp(developer_2)

mg_1.printEmps()

mg_1.removeEmp(developer_2)

mg_1.printEmps()
print('\n', mg_1.email)