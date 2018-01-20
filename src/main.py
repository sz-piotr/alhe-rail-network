from evolution import Evolution
from fitness import makefitness
from selection import selection
from crossover import crossover
from mutation import mutation_simple
from population import generate_population
import numpy as np
import networkx as nx
import matplotlib as plt
import representation
import configuration
from generator import generate_problems, Problem
from generator.generateworld import generateworld, random_locations, world_from
import random

random.seed(0)

def main2():
    path = 'problems/example'
    problem = configuration.load(path)
    solve(problem, save=True)

def main3():
    loc20 = random_locations(20)
    city_20_3 = world_from(loc20, 3)
    city_20_6 = world_from(loc20, 6)
    city_20_10 = world_from(loc20, 10)
    problems = [
        (Problem(0.1, 2, 100, 200, city_20_3), "01_u0.1t2c20p3"),
        (Problem(0.2, 2, 100, 200, city_20_3), "02_u0.2t2c20p3"),
        (Problem(0.5, 2, 100, 200, city_20_3), "03_u0.5t2c20p3"),
        (Problem(0.1, 1, 100, 200, city_20_3), "04_u0.1t1c20p3"),
        (Problem(0.1, 5, 100, 200, city_20_3), "05_u0.1t5c20p3"),

        (Problem(0.1, 2, 100, 200, city_20_6), "06_u0.1t2c20p6"),
        (Problem(0.1, 2, 100, 200, city_20_10), "07_u0.1t2c20p10"),

        (Problem(0.1, 2, 100, 200, generateworld(20, 3)), "08_u0.1t2c20p3"),
        (Problem(0.1, 2, 100, 200, generateworld(20, 3)), "09_u0.1t2c20p3"),
        (Problem(0.1, 2, 100, 200, generateworld(20, 3)), "10_u0.1t2c20p3"),
    ]
    for problem, prefix in problems:
        solve(problem, save=True, img_prefix=prefix)


def main():
    problems = generate_problems()
    for i, problem in enumerate(problems):
        print(i, len(problems), len(problem.world), problem.iterations)
        solve(problem, save=False)

def solve(problem, save=False, img_prefix=""):
    bests = []
    evolution = Evolution(
        generate_population(len(problem.world), problem.population),
        makefitness(problem.U, problem.T, problem.world),
        selection,
        crossover,
        mutation_simple,
        keep=min
    )
    before = evolution.stats()
    first = evolution.best(min)
    for i in range(problem.iterations):
        print(i)
        evolution.advance()
        bests.append(min(evolution.scores))

    after = evolution.stats()

    if(save):
        # representation.save_chart('results/' + img_prefix + 'chart.png', bests, problem.iterations)
        # representation.save_graph('results/' + img_prefix + 'first.png', problem, first)
        representation.save_graph('results2/' + img_prefix + '.png', problem, evolution.best(min))
    else:
        write_results(problem, before, after)


def write_results(problem, before, after):
    data = [
        problem.U,
        problem.T,
        problem.population,
        problem.iterations,
        len(problem.world),
        len(list(filter(lambda c: c.has_powerplant, problem.world))),
        *before,
        *after
    ]
    with open('problems/results.csv', 'a') as f:
        f.write(','.join(map(str, data)))
        f.write('\n')

if __name__ == '__main__':
    main3()
