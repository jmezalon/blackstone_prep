###################### Object Oriented Program = mimic real world object


# from car import Car

# car_1 = Car('Nissan', 'Altima', 2022, 'Red')

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

# car_2 = Car("Ford", "Mustang",2019,"Green")

# car_2.drive()

###################### Class variables

# car_1.wheels = 2 # this will only change the wheels for car 1

# Car_2.wheels = 2 # if we use capital car, it will change all instances of the car

# print(car_2.wheels)
# print(car_1.wheels)

# print(Car.wheels) # print the default numbers of wheels



###################### inheritance = parent child relationship - receive everything that the parent has
'''
class Animal:

    alive = True  

    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal sleeping")


class Rabbit(Animal):
    
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    
    def swim(self):
        print("This fish is swimming") 

class Dog(Animal):
    
    def bawk(self):
        print("This dog is bawking")


# rabbit = Rabbit()
# fish = Fish()
# dog = Dog()

# dog.sleep()
# fish.eat()
# print(rabbit.alive)

# fish.swim()
# rabbit.run()
# dog.bawk()
'''

###################### Multi-level inheritance - child class inherite from another child class

'''
class Organism:

    alive = True  

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()

'''

###################### Multiple inheritance = when a child class is derived from more than one parent class

'''
class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass  

class Hawk(Predator):
    pass 

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

rabbit.flee()
fish.flee()
fish.hunt()
hawk.hunt()


'''

###################### method overwritting 
'''
class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()

rabbit.eat() # => This rabbit is eating a carrot

'''
###################### method chainning = call multiple methods sequentially

from Jeep import Jeep

jeep = Jeep() 

# jeep.turn_on()
# jeep.drive()     # these two lines could just be one line

# jeep.turn_on().drive().brake().turn_off() # it is best to write a long method chaining like this by putting each method in a new line: n we need the \ [line continuation] to go to the next line

# jeep.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()


###################### the super function = give access to the method of a parent class, returns a temporary object of the parent class

# more notes is in the Rectangle file

from Rectangle import Square, Cube

square = Square(3,3)

cube = Cube(3,3,3)

print(square.area(), " and ", cube.volume())


######################  Abstract classes = prevent a user from creating an object of that class
# compales a user to overwrite any abstract method within any child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod # need this to make a class abstract

class Vehicle(ABC): # inherite from the abc class

    @abstractmethod # declarator
    def go(self):
        pass 

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def go(self):    # in order to create a Car or Motorcycle class we need to overwrite the go
        print('You drive the car') # method that they are inheriting from the Vehicle class

    def stop(self):
        print('this car has stopped')


class Motorcycle(Vehicle):
    
    def go(self):
        print("You drive the motorcycle")
        return self

    def stop(self):
        print('this motorcycle has stopped')

car = Car() 

moto = Motorcycle()

car.go()

moto.go().stop()

car.stop()
