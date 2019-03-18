import math

def square_plus_one(a, b):
    return a * b + 1



print(square_plus_one(2, 3))

print(square_plus_one(10, 10+10))



def quadratic(a, b, c):
    x_1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x_2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    return x_1, x_2


print(quadratic(1, 2, 3))


