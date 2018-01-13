import random
import math
from collections import namedtuple

MAX_RADIUS = 100
City = namedtuple('City', ['x', 'y', 'has_powerplant'])

def generateworld(n_cities, n_powerplants):
    return [
        random_city(i < n_powerplants)
        for i in range(n_cities)
    ]

def random_city(has_powerplant):
    r = random.uniform(0, MAX_RADIUS)
    phi = random.uniform(0, math.pi * 2)
    return City(
        r * math.cos(phi),
        r * math.sin(phi),
        has_powerplant
    )
