from evolution import Evolution
from fitness import fitness
from selection import selection
from crossover import crossover
from mutation import mutation

def main():
    evolution = Evolution(
        list(range(10)),
        fitness,
        selection,
        crossover,
        mutation
    )
    for i in range(10):
        print(evolution.population)
        evolution.advance()

if __name__ == '__main__':
    main()
