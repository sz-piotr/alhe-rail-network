from statistics import median

class Evolution:

    def __init__(self, population, fitness, crossover, mutation, selection):
        self.population = population
        self.fitness = fitness
        self.crossover = crossover
        self.mutation = mutation
        self.selection = selection
        self._evaluate()

    def _evaluate(self):
        self.scores = list(map(self.fitness, self.population))
        self.highest_score = max(self.scored)
        self.median_score = median(self.scored)

    def advance(self):
        self.population = [
            self.mutation(self.crossover(self.select(), self.select()))
            for s in scored
        ]
        self._evaluate()

    def select(self):
        self.population[self.selection(self.scores)]
