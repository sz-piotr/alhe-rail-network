from generator.generateworld import City
from generator import Problem

def load(path):
    with open(path, 'r') as f:
        U, T, population_size, iterations = f.readline().split()
        cities = [
            city_from_line(line)
            for line in f
        ]
        return Problem(
            float(U),
            float(T),
            int(population_size),
            int(iterations),
            cities
        )


def city_from_line(line):
    x, y, has_powerplant = line.split()
    return City(float(x), float(y), has_powerplant == '1')


def readTests(self, path):
    file = open(path, 'r')
    files = []
    for line in file:
        row = line.split()
        files.append(row)
    return files
