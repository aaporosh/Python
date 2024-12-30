class Transport:
    def calculate_cost(self, weight, distance):
        pass

class Truck(Transport):
    def calculate_cost(self, weight, distance):
        return weight * distance * 0.5

class Ship(Transport):
    def calculate_cost(self, weight, distance):
        return weight * distance * 0.3

class Plane(Transport):
    def calculate_cost(self, weight, distance):
        return weight * distance * 1.0

#polymorphism
transports = [Truck(), Ship(), Plane()]
weight, distance = 100, 400  

for transport in transports:
    print(f"{transport.__class__.__name__}: Delivery Cost = {transport.calculate_cost(weight, distance)}")
