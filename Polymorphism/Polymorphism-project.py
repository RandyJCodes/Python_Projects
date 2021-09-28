#
# Python: 3.9.5
#
# Author: Randall Jackson
#
#
# Purpose: Project with a parent class and 2 child classes.
# The Parent class utilizes a function.
# Child classes utilize polymorphism on the parent class method. 
# 

# Parent class
class Vehicle:
    brand = "Unknown"
    color = "Unknown"
    fuel = "Water"
    
    def information(self):
        msg = "\nBrand: {}\nColor: {}\nFuel: {}".format(self.brand,self.color,self.fuel)
        return msg

# child class
class Plane(Vehicle):
    brand = "Airbus"
    color = "White"
    fuel = "Hydrogen"
    wing-style = "Canted"
    propulsion-system = "Jet Engines
    
    def flight(self):
        msg ="\nPlanes go very fast and fly high in the sky!"
        return msg
    
# another child class
class Car(Vehicle):
    brand = "Mazda"
    color = "Blue"
    fuel = "Gasoline"
    Wheel-size = "22 inches"
    Body-kit = "Deuce Style"

    def drive(self):
        msg = "\nCars are much faster than going on foot and horseback!"
        return msg

if __name__ == "__main__":
    plane = Plane()
    print(plane.information())
    print(plane.flight())
    
    car = Car()
    print(car.information())
    print(car.drive())

    
