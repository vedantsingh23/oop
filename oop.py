class Vehicle:
    def __init__(self,max_speed,mileage,name,model,manufacturer):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        self.model = model
        self.manufacturer = manufacturer

    def __str__(self):
        return self.name + ' has a max speed of ' + str(self.max_speed) + ' with a mileage of ' + self.mileage + ' and is a ' + self.manufacturer + ' ' + self.model + ' with a capacity of ' + str(self.sc) + 'people.'

    def seating_capacity(self,sc):    
        self.sc = sc
        return "The capacity of " + self.name + " is " + str(sc)

    def fc(self,sc):
        self.sc = sc
        return "The fare charge of " +self.name + ' is $' + str(sc * 100)

class Bus:
    def __init__(self,max_speed,mileage,name,model,manufacturer, color = 'white'):
        Vehicle.__init__(self,max_speed,mileage,name,model,manufacturer)
        self.color = color
    def __str__(self):
        return self.name + ' has a max speed of ' + str(self.max_speed) + ' with a mileage of ' + self.mileage + ' and is a ' + self.manufacturer + ' ' + self.model + ' with a capacity of ' + str(self.sc) + 'people in the color ' + self.color + '.'
    def sc1(self,c = 50):
        self.c = c
        return "The capacity of " + self.name + " is " + str(c)
    def fc1(self, c = 50):
        self.c = c
        return "The fare charge of " +self.name + ' is $' + str(self.c * 100)


a=Vehicle('120','100000','bob','Jetta','VW')
print(a.seating_capacity(5))
print(a.fc(4))

b = Bus('120','100000','bob','Jetta','VW')
print(b.fc1)

            