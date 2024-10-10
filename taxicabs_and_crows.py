"""
Taxicabs and Crows
Dylan Rhymaun
Calculate the distance a bird would have to fly
and the distance a car would have to drive
to get from one point to another over a city
with a grid layout.
"""
import math

mi_streets = .05
mi_avenues = (1/7)

def taxicab_distance(streets, avenues):
    taxi = (streets * mi_streets) + (avenues * mi_avenues)
    return taxi

def crow_distance(streets, avenues):
    crow = math.sqrt(((streets * mi_streets) ** 2) + ((avenues * mi_avenues) ** 2))
    return crow

streets = int(input('how many street blocks must you travel? '))
avenues = int(input('how many avenue blocks must you travel? '))

crow_flight = crow_distance(streets, avenues)
taxi_distance = taxicab_distance(streets, avenues)
difference = taxi_distance - crow_flight

print(f'The crow\'s flight is {difference:.2f} miles shorter than riding in a taxi.')