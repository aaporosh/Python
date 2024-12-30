class Student :
    def __init__(self,name,id,department):
        self.name = name
        self.id = id
        self.department = department

    def info(self):
        print("Name :",self.name,"\nId :",self.id,
        "\nDepartment :",self.department)

S1 = Student("Abir",1814,"CSE")
S1.info()

S2 = Student()
S2.name = "Rafi"
S2.id = 1951
S2.department = "CSE"
S2.info()