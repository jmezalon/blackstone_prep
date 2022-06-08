###################### Object Oriented Program = mimic real world object


from car import Car

car_1 = Car('Nissan', 'Altima', 2022, 'Red')

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

car_2 = Car("Ford", "Mustang",2019,"Green")

# car_2.drive()

###################### Class variables

car_1.wheels = 2 # this will only change the wheels for car 1

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
###################### method chainning