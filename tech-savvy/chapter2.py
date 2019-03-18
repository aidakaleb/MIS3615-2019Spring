## Numbers

# print(3.14e-2)

# length_of_number = len(str(2**1000000))
#
# print(length_of_number)


# print(len('Maddison'))
#
# import math
#
# print(math.pi)
# print(math.sqrt(25))


import random

# print(random.random())
# print(int(random.random()*100)) # a random integer between 0 and 100
#
# print(random.randint(1, 6))  # a random integer between 1 and 6
#
# print(random.choice(["Valerie", "Aob",
#                      "Maddison", "Grace"])) # a random name in the list
#
#
# print(random.choice([2, 5, 7587]))

# lower = int(input("Please a number  as the lower bound:"))
# upper = int(input("another one as upper bound:"))
# print(random.randint(lower, upper))


## Strings
# I'm saying "OK".


# print("I'm saying \"OK\".")
#
# print('I\'m learning\n\nPython.')


## Boolean

print(3 > 2)
print(3 > 5)

print(3 > 2 and 3 > 5)
print(3 > 2 or 3 > 5 or False or 100 < 100)

age = int(input("How old are you?"))

is_in_US = True

answer = input('Are you in US?')
if answer == 'no':
    is_in_US = False

if age < 21 and is_in_US:  # boolean
    print('Sorry, you cannot.')
else:
    print('Yes, you can.')



# Exercise 3


import time
print(time.time())
current = time.time()
second = current % 60
minutes = (current//60) % 60
hours = (current//60)//60 % 24
days = current // 60 // 60 // 24
print('Current time: {:d} days, {:d} hours, {:d} minutes and {:.2f} seconds from Epoch.' .format(
    int(days), int(hours), int(minutes), second))