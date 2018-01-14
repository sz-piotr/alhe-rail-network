from evolution import Evolution
from fitness import makefitness
from selection import selection
from crossover import crossover
from mutation import mutation_simple
from population import generate_population
import configuration

def main():
    path = 'src/config'

    problem = configuration.load(path)

    evolution = Evolution(
        generate_population(len(problem.world), problem.population),
        makefitness(problem.U, problem.T, problem.world),
        selection,
        crossover,
        mutation_simple
    )

    evolution.print_stats()
    for i in range(problem.iterations):
        evolution.advance()
    evolution.print_stats()

if __name__ == '__main__':
    main()
