class student():
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

    def display(self):
        print(f'Name : {self.name}\n Id : {self.id} \nAge : {self.age}')

class Undergraduate(student):
    def __init__(self, name, id, age ,tuition_fee,credit):
        super().__init__(name, id, age)
        self._tuition_fee = tuition_fee
        self.__credit = credit


    def set_credit(self,total_credit):
        self.__credit= total_credit
    
    def get_credit(self):
        return self.__credit

    def display(self):
        print(f'Name : {self.name} \n Id : {self.id} \nAge : {self.age} \nTuition Fee : {self._tuition_fee} \nCredit : {self.get_credit()} ')
    
    def calculate_fee(self,fee):
        return f'Calculate Fee : {self.get_credit()*fee}'


s1 = student("Abir",1814,22)

s1.display()

U1 = Undergraduate("Sohi",1917,22,12000,150)
U1.set_credit(140)
U1.display()
print(U1.calculate_fee(10))

