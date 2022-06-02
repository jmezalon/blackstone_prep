###################### str.format() = optional method that gives users more control when displaying output

animal, item = 'cow', 'moon'

# print("the "+animal+" jumped over the "+item) 
# print("the {} jumped over the {}".format(animal, item)) # {} function as a placeholder for your format args
# print("the {1} jumped over the {0}".format(animal, item)) # positional argument
# print("the {animal} jumped over the {item}".format(animal='cow', item='moon')) # keyword arguments

text = "The {} jumped over the {}"
# print(text.format(animal,item))

name = "Max"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:5}, nice to meet you!".format(name)) # if we want to add padding to our argument, default is right
# print("Hello, my name is {:<5}, nice to meet you!".format(name)) # if we want to add right padding to our argument
# print("Hello, my name is {:>5}, nice to meet you!".format(name)) # if we want to add left padding to our argument
# print("Hello, my name is {:^5}, nice to meet you!".format(name)) # if we want to center our argument


# number = 3.1413422
# number = 1000

# print("The number pi is {:.3f}".format(number)) # display the first 3 digits after the decimal and round your number
# print("The number is {:,}".format(number)) # add a comma after the thousands place
# print("The number is {:b}".format(number)) # change to binary
# print("The number is {:o}".format(number)) # octo
# print("The number is {:X}".format(number)) # Hexodecimal, lower or upper case arg
# print("The number is {:e}".format(number)) # scientific notation, lower or upper case arg



###################### the random module