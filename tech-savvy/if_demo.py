# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')
#
#

def countdown(n):
    import time
    time.sleep(1)

    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

# countdown(5)


def countdown2(n):
    import time
    time.sleep(.0005)

    print(n)
    countdown2(n-1)

# countdown2(5)



def fab(n):
    """
    this function will return the nth Fabonacci number.

    """
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-2) + fab(n-1)


for i in range(1, 11):
    print('The {}th Fabonacci number is {}.'.format(i,fab(i)))
