def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        print('now we are checking {}. flag is {}.'.format(c, flag))

    return flag


# print(any_lowercase3('iPhonE'))


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()

        print('now we are checking {}. flag is {}.'.format(c, flag))
    return flag


# print(any_lowercase4('iPAD'))
# print(any_lowercase4('python'))


def any_lowercase5(s):
    for c in s:
        print('now we are checking {}. flag is {}.'.format(c, c.islower()))
        if not c.islower():
            return False
    return True


# print(any_lowercase5('python'))
# print(any_lowercase5('BABSON'))


def sum_double(a, b):
    if a != b:
        result = a + b
    else:
        result = (a + b) * 2
    return result


# print(sum_double(1, 2))
# print(sum_double(2, 2))

print(chr(ord('b') + 3))

str1 = 'helloworld'
print(str1[::-1])

url = 'www.api.com/q={query}&key={KEY}'
print(url.format(KEY='123456', query="Babson"))