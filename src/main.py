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
from generator.generateworld import generateworld

def main2():
    path = 'problems/example'
    problem = configuration.load(path)
    solve(problem, save=True)

def main3():
    problem = Problem(0.1, 2, 100, 100, generateworld(20, 3))
    solve(problem, save=True, img_prefix="u0.1_t2_p100_i1000_c20.3_k2_")

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
        representation.save_chart('results/' + img_prefix + 'chart.png', bests, problem.iterations)
        representation.save_graph('results/' + img_prefix + 'first.png', problem, first)
        representation.save_graph('results/' + img_prefix + 'best.png', problem, evolution.best(min))
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
