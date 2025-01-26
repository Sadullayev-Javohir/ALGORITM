"""Vehicle class ini yarating. Class ning xususiyatlari maxSpeed
va mileage. Endi bu class larga parametr yuklang va chop eting."""

class Vehicle:
    
    def __init__(self, maxSpeed, mileage):

        self.maxSpeed = maxSpeed
        self.mileage = mileage
       
modelX = Vehicle(200, 17)

print(modelX.maxSpeed, modelX.mileage)