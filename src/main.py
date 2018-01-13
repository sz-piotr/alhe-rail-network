from evolution import Evolution
from fitness import fitness
from selection import selection
from crossover import crossover
from mutation import mutation
import loadconfiguration

def main():
    evolution = Evolution(
        list(range(10)),
        fitness,
        selection,
        crossover,
        mutation
    )
    #path = '../src/config'
    #testconfig = loadconfiguration.loadConfig(path)
    #points = loadconfiguration.loadPoints(path)


    print(evolution.population)
    for i in range(100):
        evolution.advance()
    print(evolution.population)

if __name__ == '__main__':
    main()
