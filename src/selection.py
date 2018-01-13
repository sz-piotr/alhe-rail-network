import random
import math

def selection(scores):
    sorted_by_fitness = sorted(enumerate(scores), key=second_element)
    index = math.floor(random.triangular(0, len(scores), 0))
    return sorted_by_fitness[index][0]

def second_element(tuple):
    return tuple[1]
