from evolution import Evolution
from fitness import fitness
from selection import selection
from crossover import crossover
from mutation import mutation
import populationgenerator
import loadconfiguration

def main():
    path = '../src/config'
    testconfig = loadconfiguration.loadConfig(path)
    points = loadconfiguration.loadPoints(path)

    evolution = Evolution(
        populationgenerator.generate_population(populationgenerator.generate_single_tree(points), 10),
        fitness,
        selection,
        crossover,
        mutation
    )

    print(evolution.population)
    for i in range(100):
        evolution.advance()
    print(evolution.population)

if __name__ == '__main__':
    main()
