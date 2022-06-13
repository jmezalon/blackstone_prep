###################### Higher order functions = accept a func as an argument / or return a func as an output


def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func('Hello')
    print(text)


# hello(loud)
# hello(quiet)

# this is returning a function

def divisor(x):
    def divident(y):
        return y / x  
    return divident


# divide = divisor(2) # this return divident and save it to divide
# print(divide(10)) # this call divident while divisor still stores the number 2


###################### lambda function = function written in 1 line using lambda keyword
#                                       accepts any number of arguments, but only has one expression.

# lambda parameters:expression

# def double(x):
#     return x * 2

# lambda

double = lambda x: x * 2

# print(double(2))

multiply = lambda x, y: x * y

# print(multiply(2,4))

full_name = lambda first_name, last_name: first_name+" "+last_name

# print(full_name('jean','mezalon'))

age_check = lambda age:True if age >= 18 else False 

# print(age_check(47))


###################### sorting functions

# students = ['max', 'christie', 'jadison', 'trina']


# two keyword we could pass in, key or reverse. i.e reverse=True
# students.sort()

# sorted_students = sorted(students, reverse=True)

# for x in sorted_students:
#     print(x)


# keyword argument

# sort does not work with tuples

# students = [('max', 'F', 60),
            #  ('christie','A',90), 
            #  ('jadison','C',70), 
            #  ('trina', 'B',85)]

# grade = lambda grades:grades[1]

# students.sort(key=grade)

# for x in students:
#     print(x)


# if we have a tuple, we would do it like this:

students = (('max', 'F', 31),
             ('christie','A',23), 
             ('jadison','C',25), 
             ('trina', 'B',27))
age = lambda ages:ages[2]

sorted_students = sorted(students, key=age)

# for x in sorted_students:
#     print(x)

