class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class PermanentEmployee(Employee):
    def __init__(self, name, id, fixed_salary):
        super().__init__(name, id)
        self.fixed_salary = fixed_salary

    def Calculate_salary(self):
        return self.fixed_salary

class ContractEmployee(Employee):
    def __init__(self, name, id, hour, salary):
        super().__init__(name, id)
        self.hour = hour
        self.salary = salary

    def Calculate_salary(self):
        return self.hour * self.salary

#Creating Permanent Employee Object
permanent_employee = PermanentEmployee("Abir", 1814, 50000)
print("Name:", permanent_employee.name, "\nId:", permanent_employee.id, "\nSalary:", permanent_employee.Calculate_salary())

#Creating Contract Employee Object
contract_employee = ContractEmployee("Rafi" , 1951, 8,400)
print("\n\nName : ",contract_employee.name,"\nId : ",contract_employee.id,"\nWorking Hour : ",contract_employee.hour,"\nSalary : ",contract_employee.Calculate_salary())