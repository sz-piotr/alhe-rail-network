from evolution import Evolution
from fitness import makefitness
from selection import selection
from crossover import crossover
from mutation import mutation_simple
from population import generate_population
import configuration

def main():
    path = 'problems/example'
    problem = configuration.load(path)
    solve(problem)

def solve(problem):
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
    after = evolution.stats()
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
    print(data)
    with open('problems/results.csv', 'a') as f:
        f.write(','.join(map(str, data)))
        f.write('\n')

if __name__ == '__main__':
    main()
