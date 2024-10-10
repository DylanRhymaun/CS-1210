"""
Quadratic Solver
Dylan Rhymaun
A program that finds the root(s) of a
quadratic polynomial of the form
a x ** 2 + b x + c = 0
"""
import math

def calc_discriminant(a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    return float(discriminant)

if __name__ == '__main__':


    a = int(input('Enter a value for a: '))
    b = int(input('Enter a value for b: '))
    c = int(input('Enter a value for c: '))

    d = calc_discriminant(a, b, c)
    

    if d > 0:
        root1 = ((-b + math.sqrt(d)) / (2 * a))
        root2 = ((-b - math.sqrt(d)) / (2 * a))
        print(f'The two roots of the equation are {root1:.3f} and {root2:.3f}')

    elif d == 0:
        root_negative = -b / (2 * a)
        print(f'There is one real root to this equation: {root_negative:.3f}')

    else:
        print('There are no real roots to this equation')
