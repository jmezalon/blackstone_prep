###################### How to accept users input

# input will always be a string, remember we cannot do math operations on str or combine str with int
# always pay attention to what type of input you are requesting

# name = input('What is your name?: ')

# print('Hello '+name)

# age = int(input('How old are you?: '))

# age+=1

# print(f'next year you will be {age} years old')

###################### function with the math module

# import math # need to import math to use the module avaible

pi = 3.14

x, y, z = 1,7,3

# print(round(pi)) # => 3 / don't use math
# print(math.ceil(pi)) # => 4
# print(math.floor(pi)) # => 3
# print(abs(pi)) # => 3.14 / don't use math
# print(math.pow(pi,2)) # => 9.8596
# print(math.sqrt(81)) # => 9.0
# print(max(x,y,z)) # => 7
# print(min(x,y,z)) # => 1


###################### string slice in python

# two methods, indexing[]          or         slice()
            #  [start:stop:step]
            # start is inclusive, stop is exclusive
            # if you leave out start, [:stop] start is implicit
            # same thing for stop, [start:] stop is implicit
            # step just skip by the amount you entered
            # you can leave out start and stop, but make sure you add two colins, [::step]

            # if you want to reverse a string you would use step like so, name[::-1]

name = "Max Mezalon"

reversed_name = name[::-1]

# print(reversed_name)

# slice works like so, still have start,stop,step, exept we use commas

website = 'https://afro-fete.herokuapp.com'
website2 = 'https://google.com'

# # this is the slice function
slice = slice(8,-4)

# # we use it like so
# print(website[slice])
# print(website2[slice])


###################### if statements = block of code that will execute if a condition is true

# age = int(input('How old are you?: '))

# if age == 100:
#     print('You are a century old!')
# elif age >= 18:
#     print('You could drive!')
# else:
#     age_left = 18 - age
#     print(f"you have {age_left} years to start driving!")


###################### logical operators (and,or,not)

# temp = int(input('What is the temperature outside?: '))

# if not(temp >= 0 and temp <= 30):
#     print('The temperature is bad today!')
#     print('stay inside!!!')
# elif not(temp < 0 or temp > 30):
#     print('the temperature is good today!')
#     print('Go outside!!!')



###################### while loop, keep going while a condition is true


# name = "" # name = None / does the same thing

# while len(name) == 0: # not name / does the same thing
#     name = input("Enter your name: ")

# print(name+ ", Nice name!")


###################### for loop, count down timer

# for i in range(10): # + 1 here, gives 0 - 10
#     print(i+1) # gives us 1 to 10

# for i in range(0,6+1,2):
#     print(i)

# with string

# for i in "Max Mezalon":
#     print(i)

# import time 

# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1) # count 1 second
# print("Happy New Year!")


###################### Nested Loop

# end="" stops it from going to a new line for print

# rows = int(input('How many rows?: '))
# colums = int(input('How many colums?: '))
# symbol = input('Enter a symbol to use: ')

# for i in range(rows):
#     for j in range (colums):
#         print(symbol, end="")
#     print()



######################  Loop control statements, break - continue - pass

# BREAK, stops the loop

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# CONTINUE, skips over

# phone_number = "123-432-0239"

# for i in phone_number:
#     if i == '-':
#         continue
#     print(i, end="")


# PASS, does nothing and acts like a place holder

# for i in range(6,19):

#     if i == 13:
#         pass 
#     else:
#         print(i)