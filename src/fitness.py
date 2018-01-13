import math

def makefitness(U, T, cities)
    powerplants = filter(lambda city: city.has_powerplant, cities)
    electicity_costs = [electicity_cost(city, powerplants, U) for city in cities]

    def fitness(specimen):
        sum = 0
        for v1, v2 in specimen.edges():
            distance_penalty = distance(cities[v1], cities[v2]) * T
            min_cost = min(electicity_costs[v1], electicity_cost[v2])
            sum += distance_penalty + min_cost
        return sum

    return fitness

def electicity_cost(city, powerplants, U):
    min_distance = min([distance(city, plant) for plant in powerplants])
    return distance ** (1 + U)


def distance(city, other):
    return math.sqrt((city.x - other.x) ** 2 + (city.y - other.y) ** 2)
