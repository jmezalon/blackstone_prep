###################### Pass object into methods

'''
class Car:

    color = None 


class Motorcycle:

    color = None


def change_color(vehicle, color):

    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()


change_color(car_1, 'Blue')
change_color(car_2, 'Red')
change_color(car_3, 'Yellow')
change_color(bike_1, 'Orange')


print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)


'''

###################### duck-typing = concept where the class of an object is less important than 
#                                  the mehods/attributes. class type is not checked if minimum methods/att #                                  are present.

'''
class Duck:

    def walk(self):
         print("This duck is walking")

    def talk(self):
         print("This duck is Qwuacking")


class Chicken:

    def walk(self):
         print("This chicken is walking")

    def talk(self):
         print("This chicken is Clucking")


class Person:

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter!")


duck = Duck()
chick = Chicken()
person = Person()

person.catch(duck)
person.catch(chick) # if we pass in chicken it will still work, bc chick has both the talking and walking methods


'''

###################### walrus operator := 

# new to python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True  

# print(happy := True) # assign and use in one expression

# foods = list()

# while True:
#     food = input('what food do you like?: ')
#     if food == 'quit':
#         break 
#     foods.append(food)

# print(foods)


# with the walris operator we can use less lines of code

# foods = list()

# while food := input('what food do you like?: ') != "quit":
#     foods.append(food)


# print(foods)


###################### assign a function to a variable

def hello():
    print('Hello')


hi = hello # when we don't call it we are assigning the memory address of helo to hi

hi() # so when we call hi, it's as if we were calling hello

say = print 

say("I assign the memory of print to say!!!")