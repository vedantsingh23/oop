class Vehicle:
    def __init__(self,max_speed,mileage,name,model,manufacturer):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
    

class Bus(Vehicle):
    def __init__(self,color, fare_charge):
        self.color = color
        self.fare_charge = fare_charge