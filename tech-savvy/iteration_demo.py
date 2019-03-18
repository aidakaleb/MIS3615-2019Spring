# sum = 0
# for number in range(1, 1001):
#     print('in the {}th iteration, current number is {}, sum is {}'.format(number, number, sum))
#     sum = sum + number
#     print('\t after adding number, the new sum is {}\n'.format(sum))
#
# print(sum)

# sum = 0
# for i in range(1, 11):
#     print('in the {}th iteration, current i*i is {}, sum is {}'.format(i, i*i, sum))
#     sum = sum + i*i
#     print('\t after adding square of i, the new sum is {}\n'.format(sum))
#
# print(sum)

# Calculate the value of your name, if we say 'a' is worth 1
# 'z' is worth 26.

# total_value =0
# name = 'valerie'
#
#
# for letter in name:
#     # print('current letter is worth {}.\n'.format(ord(letter)-96))
#     total_value = total_value + (ord(letter)-96)
#
# print('The value of name {} is {}.'.format(name, total_value))


#
# def countdown(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#         import time
#         time.sleep(1)
#
#     print('Blastoff!')
#
# countdown(-1)


result = 0
for number in range(1, 1001):
    if number % 2 == 1: # this means number is an odd number
        result = result + number

print(result)
