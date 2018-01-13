import random

def mutation(specimen):
    return abs(specimen + random.uniform(-0.1, 0.1))
