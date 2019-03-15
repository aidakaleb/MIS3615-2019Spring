# print("hello, world!")

# print("hello, class!")
#
# print(2019 - 2000)
#
# print(-2  + 100)

# print('Hey Jude,', "Don't make it bad")
#
# print('1 + 2 + 3 =', 1+2+3)

# name = input()
#
# print('Hello, ', name)

# a = 'ABC'
# b = a
# a = 'XYZ'
#
# print('a is', a, '. b is ', b)


first_name = 'John'
last_name = 'Lennon'
name = first_name + " " + last_name

# print(first_name * 20)

# print('hello,', name)
# print('hello, {}! You are {} years old.'.format(name, 20))

template = 'Hello, {}! You are {} years old.'

name1 = 'Grace'
age1 = 20

name2 = 'Aida'
age2 = 18

print(template.format(name1, age1))

print(template.format(name2, age2))

print('Pi equals {:.2f}'.format(3.1415926))






template = 'Hello, {name}! You are {age} years old.'

print(template.format(age=age1, name=name1))

import math

print(math.pow(math.pi, 5))
print(math.pi)


print(2**38)