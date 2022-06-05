######################   list = used to store multiple items in a single variable

# food = ['Mac & Cheese', 'Pizza', 'Rice and Chicken', 'Hot Dog']

# print(food[-1]) # print last element
# update like so, food[0] = 'something else'

# some methods for list 
# append
# food.append('ice cream')

# remove
# food.remove('Pizza')

# remove last
# food.pop()

# insert
# food.insert(1,"Cake")

# sort
# food.sort()

# food.clear will remove all the elements in the list
# print(food)

# to print list element

# for x in food:
#     print(x)


###################### 2D list, multi-dementialnal list

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# desert = ["cake", "ice cream"]

# food = [drinks, dinner, desert]

# print(food[2][1])


###################### tuple = ordered and we can't change them

student = ("Max",31,"male")

# print(student.count("Max"))
# print(student.index("male"))

# iterate through tupple 

# for x in student:
#     print(x)

# if "male" in student:
#     print("Student is a male")
# else:
#     print("Student is a female")


###################### set - what is it in python - unordered and unindex with no duplicates
# faster than list 

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "fork"}

# methods for set
# add 
# utensils.add("napkin")
# remove
# utensils.remove("fork")
# clear
# utensils.clear()

# combine sets
# utensils.update(dishes)

# we could join them to a brand new set
# dinner_table = utensils.union(dishes)

# compare and find difference
# print(utensils.difference(dishes))

# show what they have in common
# print(dishes.intersection(utensils))

# for x in dinner_table:
#     print(x)


###################### dictionary = changeable unordered collection of key value pair 
                                    # fast because they use hashing, allow us to acces a value quickly

capitals = {
    'USA': 'Washington DC',
    'India': 'New Dehli',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

# print(capitals['Russia'])
# get is better because if the key doesn't exist it will return none instead of an error message that could break your code # =>
# print(capitals.get('Haiti')) 

# to list all the keys
# print(capitals.keys())

# values
# print(capitals.values())

# to print keys and values
# print(capitals.items())

# update method
# capitals.update({"Haiti": "Port-Au-Prince"})
# you could change an existing value in similar way 

# remove a key value pair
# capitals.pop('India')

# clear the dictionary with 
# capitals.clear()

# to list using a for loop
# for key,value in capitals.items():
#     print(key,value)


###################### index operator [] = gives access to a sequence's element (str, list, tuples)

# name = 'max Mezalon'

# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name[:3].upper()
# last_name = name[4:].lower() # we could also use -negative indexing 
# last_char = name[-1] # => n

# print(last_name)