###################### __name__ == '__main__':

# 1. module can be run as a standalone program
#                   or
# 2. module can be imported and used by other modules

# python interpreter sets 'special variables', one of which is __name__
# python will assign the __name__ variable a value of '__main__ if it's
# the initial module being run

# def main():
#     print('Hello!')

# if __name__ == '__main__':
#     main()


###################### time module

import time  

print(time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string
#                   epoch = when your computer thinks time began (reference point)

print(time.time()) # returns current seconds since epoch


print(time.ctime(time.time())) # gives current time could also use localtime()

time_object = time.localtime()

local_time = time.strftime('%B %d %Y %H:%M:%S', time_object)

print(local_time)


time_string = '20 May, 2013'

time_obj = time.strptime(time_string, '%d %B, %Y')

print(time_obj)

#     (year,month,day,hours,minutes,secs,#day of the week, #day of the year, dst
time_tuple = (2020,4,30,12,45,23,0,0,0)

time_str = time.asctime(time_tuple)

print(time_str)

