from statistics import median

class Evolution:

    def __init__(self, population, fitness, selection, crossover, mutation, keep):
        self.population = population
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.keep = keep
        self._evaluate()
        self.iterations = 0

    def _evaluate(self):
        self.scores = list(map(self.fitness, self.population))

    def advance(self):
        self.iterations += 1
        self.population = [self.best(self.keep)] + [
            self.mutation(self.crossover(self.select(), self.select()))
            for i in range(len(self.population) - 1)
        ]
        self._evaluate()

    def select(self):
        return self.population[self.selection(self.scores)]

    def stats(self):
        return (min(self.scores), mean(self.scores), max(self.scores))

    def print_stats(self):
        print('iterations', self.iterations)
        print('min', min(self.scores))
        print('mean', mean(self.scores))
        print('max', max(self.scores))

    def best(self, fn):
        return self.population[self.scores.index(fn(self.scores))]

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
