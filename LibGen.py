import readInput
from pyeasyga import pyeasyga

# define a fitness function
def fitness(individual, data):
    weight, volume, price = 0, 0, 0
    for (selected, item) in zip(individual, data):
        if selected:
            weight += item[0]
            volume += item[1]
            price += item[2]
    if weight > readInput.weight or volume > readInput.volume:
        price = 0
    return price

def runGen():
    data=readInput.things
    ga = pyeasyga.GeneticAlgorithm(data)        # initialise the GA with data
    ga.population_size = 200                    # increase population size to 200 (default value is 50)
    ga.fitness_function = fitness  # set the GA's fitness function
    ga.run()  # run the GA
    return ga.best_individual()  # print the GA's best solution