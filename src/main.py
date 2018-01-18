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
from generator import generate_problems

def main2():
    path = 'problems/example'
    problem = configuration.load(path)
    solve(problem, save=True)

def main():
    problems = generate_problems()
    for i, problem in enumerate(problems):
        print(i, len(problems))
        solve(problem, save=False)

def solve(problem, save=False):
    bests = []
    evolution = Evolution(
        generate_population(len(problem.world), problem.population),
        makefitness(problem.U, problem.T, problem.world),
        selection,
        crossover,
        mutation_simple
    )
    before = evolution.stats()
    for i in range(problem.iterations):
        evolution.advance()
        bests.append(min(evolution.scores))

    after = evolution.stats()

    if(save):
        representation.save_chart('results', bests, problem.iterations)
        representation.save_graph('results', problem, evolution.population[evolution.scores.index(min(evolution.scores))])
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
    main()
