###################### map() function 

# map(function, iterable)

store = [('shirt',10.00),
         ('pants',15.90),
         ('jacket',50.00),
         ('skirt',13.00)]

to_euros = lambda data: (data[0], data[1]*0.82)
# to_dollars = lambda data: (data[0], data[1]/0.82)

store_euros = list(map(to_euros, store))

store_dollars = map(lambda data: (data[0], round(data[1]/0.82, 2)), store_euros) # one line

# for i in store_dollars:
#     print(i)


# print('{:.2f}'.format(9.423)) # round using format
# print(round(9.245, 2)) # round using round method


# print(list(map(lambda x: x*2,[2,4,3])))


###################### filter() function
# filter(function, iterable)

friends = [('rachel',10),
            ('binee',42),
            ('lockie',25),
            ('john',17)]

can_drink = list(filter(lambda x: x[1] >= 18, friends))

# altinatively, this can be written like this:

# age = lambda x: x[1] >= 18

# can_drink = list(filter(age, friends))

# for i in can_drink:
#     print(i)


###################### reduce() function

# reduce(function, iterable)

import functools

letters = ['H','E','L','L','O']

word = functools.reduce(lambda x,y: x+y,letters)

# print(word)

factorial = [5,4,3,2,1]

result = functools.reduce(lambda x,y: x * y, factorial)

# print(result)


###################### list comprehension = a way to create a new list with less syntax
#                                               list = [expression for item in iterable]
#                       list with conditions    list = [expression for item in iterable, if conditional]
#                       list with if/else       list = [expression (if/else) for item in iterable]


squares = [i * i for i in range(1,11)] # if we were not using list comprehension, this is 3 lines:

# squares = []
# for i in range(1,11):
#     squares.append(i * i)

# print(squares)

students = [100, 10, 80, 70, 60, 50, 40, 130, 80]

# passed_students = list(filter(lambda x: x>=60, students))
passed_students =  [grades for grades in students if grades >= 60]  

# with if else
fail_pass_students = [grades if grades >= 60 else 'Failed' for grades in students]

# print(passed_students)
# print(fail_pass_students)


###################### dictionary comprehension 

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}

cities_in_F = {'NY':30,'LA':69,'TX':78}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

# print(cities_in_C)

cities_wheather = {'NY': 'sunny','LA':'cloudy','TX':'sunny'}

sunny_cities = {key: value for (key,value) in cities_wheather.items() if value == 'sunny'}

# print(sunny_cities)

des_cities = {key: ('WARM' if value >= 70 else 'COLD') for (key,value) in cities_in_F.items()}

# print(des_cities)

def check_temp(value):
    if value >=70:
        return 'HOT'
    elif 69 >= value >= 40:
        return 'WARM'
    else:
        return 'COLD'

desscript_cities = {key: check_temp(value) for (key,value) in cities_in_F.items()}

# print(desscript_cities)


###################### zip(*iterables) = aggregate elements from 2 or more iterables 
#                                           (list, tuples, sets, etc.)
#                                       create a zip object with paired elements stored in tuples for each el


usernames = ['max', 'John', 'Cameron']
passwords = ('p@ssword', 'abc123', 'guess')
login_date = ['1/1/2022','1/23/2022','2/30/2022']

users_date = list(zip(usernames, passwords, login_date))
users = dict(zip(usernames, passwords))

# for i in users_date:
#     print(i)

# for key,value in users.items():
#     print(key+" "+value)