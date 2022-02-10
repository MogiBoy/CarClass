print("Regular car:")

class Car(object):
    condition = "new"
    print("My condition is " + condition + ".")
    
    def __init__(self, model, color, mpg, condition):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.condition = condition

    def display_car(self):
        #print (self.model, self.color, self.mpg)
        print ("I am a " + self.model + " and I am " + self.color + ". I can go " + self.mpg + " miles on one gallon.")

    def drive_car(self):
        print ("Oh no! My condition is now " + self.condition + ".")


my_car = Car("DeLorean", "silver", "88", "used")
my_car.display_car()
my_car.drive_car()

print()

print("Electric car:")

class E_Car(Car):
    condition = "new"
    print("My condition is " + condition + ".")
    
    def __init__(self, model, color, mpc, condition, battery):
        self.model = model
        self.color = color
        self.mpc = mpc
        self.condition = condition
        self.battery = battery
        
    def display_ecar(self):
        print ("I am a " + self.model + " and I am " + self.color + ". I can go " + self.mpc + " miles on one charge. " + "I have a " + self.battery + " battery.")
        
    def drive_ecar(self):
        print ("Oh no! My condition is now " + self.condition + ".")


my_ecar = E_Car("Tesla Model S", "red", "400", "like new", "molten salt")
my_ecar.display_ecar()
my_ecar.drive_ecar()