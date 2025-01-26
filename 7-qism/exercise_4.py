class Vehicle:
    
    def __init__(self, name, maxSpeed, mileAge):

        self.name = name
        self.maxSpeed = maxSpeed
        self.mileAge = mileAge
    
    def SeatingCapacity(self, capacity):
        
        return f"{self.name}ning o'rindiqlar soni {capacity}"
    
class Bus(Vehicle):
    
    def SeatingCapacity(self, capacity = 50):

        return super().SeatingCapacity(capacity=50)


bus1 = Bus("School Volvo", "189", 18)
print(bus1.SeatingCapacity())
        