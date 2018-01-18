from collections import namedtuple
from .generateworld import generateworld

REPEAT_COUNT = 5
CITY_COUNTS = [5, 20, 50, 100]
POWER_PLANT_RATIOS = [0, 0.2, 0.5, 0.7]
U_VALUES = [0.05, 0.10, 0.15]
T_VALUES = [1, 2, 5, 10]
POPULATION_COUNTS = [10, 100]
ITERATION_COUNTS = [100, 1000]

Problem = namedtuple('Problem', ['U', 'T', 'population', 'iterations', 'world'])

def generate_problems():
    worlds = [
        generateworld(n_cities, 1 + powerplant_ratio * n_cities)
        for i in range(REPEAT_COUNT)
        for n_cities in CITY_COUNTS
        for powerplant_ratio in POWER_PLANT_RATIOS
    ]
    return [
        problem
        for world in worlds
        for problem in generate_problems_with(world)
    ]

def generate_problems_with(world):
    return [
        Problem(U, T, population, iterations, world)
        for U in U_VALUES
        for T in T_VALUES
        for population in POPULATION_COUNTS
        for iterations in ITERATION_COUNTS
    ]
