from statistics import median

class Evolution:

    def __init__(self, population, fitness, selection, crossover, mutation):
        self.population = population
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self._evaluate()

    def _evaluate(self):
        self.scores = list(map(self.fitness, self.population))

    def advance(self):
        self.population = [
            self.mutation(self.crossover(self.select(), self.select()))
            for s in self.population
        ]
        self._evaluate()

    def select(self):
        return self.population[self.selection(self.scores)]
