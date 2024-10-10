"""
Sphere.py
Dylan Rhymaun
Calculate the surface area and volume of a Sphere
"""
import math

def surface_area(r):
    A = 4 * math.pi * (r ** 2)
    return A

def volume(r):
    V = (4 / 3) * math.pi * (r ** 3)
    return V

r = input('What is the radius? ')
r = float(r)
A = surface_area(r)
print(f'The surface area of a sphere with a radius of {r} is {A:.2f}')
V = volume(r)
print(f'The volume of a sphere with a radius of {r} is {V:.2f}')
