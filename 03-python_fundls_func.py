###################### functions = a block of code which is executed only when it is called.

# from audioop import mul
# from cgitb import text


def hello(name='Hi'):
    print(f'{name}, how are you?')

# hello()
# hello('Max')


###################### return statement = send pythons values/object back to the caller

def multiplier(x,y):
    return x * y 

x = multiplier(5,8)
# print(x)


###################### Keyword arguments = preceded by an identifier when we pass them to a function, order doesn't matter, different from positional arguments

def hello_example_two(first,middle,last):
    print(f'Hello, {first} {middle} {last}')

# hello_example_two(last="Mezalon", first="Max", middle="J.")


###################### nested function calls = functions calls inside of other function calls

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# we can write this in one line of code 

# print(round(abs(float(input("Enter a whole positive number: ")))))


###################### variable scope = the region that a variable is recognize 

# name = 'Max' # this is a global variable because it is outside of the fuction

def display_name():
    name = 'Mezalon' # local scope because it is define inside of the function => local variable
    print(name)

# we use local variables, before moving to global variables, i,e, Local Enclosing Global Built-in (LEGB)
# display_name()


###################### *args = pack all arguments into a tuple, can accept a varying amount of arguments

def add(*args):
    sum = 0
    # args = list(args) # to change one of the arguments we would need to caste the tuple into a list
    # args[0] = 0 # will change the first argument to 0
    for i in args:
        sum += i
    return sum

# print(add(2,5,4,5))


###################### **kwargs = parameter that will pack all arguments into a dictionary, varying amount of keyword arguments

def hello_ex_three(**kwargs):
    # print('Hello '+kwargs['first']+" "+kwargs['last'])
    print('Hello',end=", ")
    for key,value in kwargs.items():
        print(value,end=" ")

# hello_ex_three(title='Mr.', first='Max', middle='J.', last='mezalon')


