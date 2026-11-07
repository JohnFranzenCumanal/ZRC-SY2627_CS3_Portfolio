
# ACTIVITY 2: 
# 1. Answer the following questions:

# 1a. What is duck typing, as explained in the video?
#Duck typing = Another way to achieve polymorphism besides Inheritance.
# Object must have the minimum necessary attributes/methods.
# "If it looks like a duck and quacks like a duck, it must be a duck."

# 1b. What did the Car class need to have so it could work inside the same loop
# as Dog and Cat, even if it does not inherit from the Animal class?
# The Car class needed to have the same speak() method as Dog and Cat.


# 2. Create the Python code:

# 2a. Create three classes with their own move() methods.

class Car:
    def move(self):
        print("The car drives on the road.")


class Boat:
    def move(self):
        print("The boat sails on water.")


class Drone:
    def move(self):
        print("The drone flies in the sky.")


def start_trip(vehicle):
    vehicle.move()



car = Car()
boat = Boat()
drone = Drone()


vehicles = [car, boat, drone]

for vehicle in vehicles:
    start_trip(vehicle)


# 3. How does the code in 2.2 demonstrate polymorphism?
# The code demonstrates polymorphism because the same function, start_trip(),
# can accept different objects and execute their respective move() methods,
# producing different outputs.
