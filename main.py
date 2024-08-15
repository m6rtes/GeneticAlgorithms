#OBJECTIVE: MAKE AN INDIVIDUAL WITH THE MAX NUMBER PRESENT IN 'GENES' IN EVERY ONE OF ITS POSITIONS

import random

genes = [0,1,2,3,4,5,6,7,8,9]

points = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,6,10,12,14,16,27]

POPULATION_SIZE = 100
MUTATION_PROB = 0.5
INDIVIDUAL_SIZE = 7

def createIndividual():
    array = []
    for i in range(0,INDIVIDUAL_SIZE):
        array.append(random.choice(genes))
    fitness = calculate_fitness(array)
    return(array,fitness)

def initialize_Population(size):
    population = []
    for i in range(0,size):
        population.append(createIndividual())
    return population

def calculate_fitness(individual):
    fitness = 0
    for i in range(0,len(individual)):
        fitness += max(genes)-individual[i]
    return fitness

def createOffsprings(parent1, parent2):
    child = []
    parent1_choices = parent1[0][int((INDIVIDUAL_SIZE/2)-1):int((INDIVIDUAL_SIZE-(INDIVIDUAL_SIZE/2)-1))]
    parent2_choices = parent2[0][0:int((INDIVIDUAL_SIZE/2)-1)].extend(parent2[0][int(INDIVIDUAL_SIZE-(INDIVIDUAL_SIZE/2)-1):INDIVIDUAL_SIZE])
    for i in range(0,INDIVIDUAL_SIZE):
        prob=random.random()
        if prob+1 >= 1-MUTATION_PROB:
            child.append(random.choice(genes))
        elif i<(INDIVIDUAL_SIZE/2):
            child.append(random.choice(parent1_choices))
        else:
            child.append(random.choice(parent2_choices))
    fitness = calculate_fitness(child)
    return(child,fitness)        


#Get initial population
gen = 1
population = initialize_Population(POPULATION_SIZE)

running = True

while running:
    #Sort them by fitness
    sorted_population = sorted(population, key=lambda ind: ind[1])

    #When most optimal is found
    if sorted_population[0][1] <= 0:
        running = False
        break

    new_gen = []

    #Pass 5% of previous generation to new generation
    five_percent = int((POPULATION_SIZE*10)/100)
    new_gen.extend(sorted_population[:five_percent])

    #Fill other 90% of new generation with offsprings between best 40% of population
    ninety_percent = int((POPULATION_SIZE*90)/100)
    for i in range(0,ninety_percent):
        child = createOffsprings(random.choice(sorted_population[:40]), random.choice(sorted_population[:40]))
        new_gen.append(child)
    
    population = new_gen

    print(f"Generation: {gen}   Individual: {population[0][0]}  Fitness: {population[0][1]}")
    gen += 1    #Next generation

print(f"Generation: {gen}   Individual: {sorted_population[0][0]}  Fitness: {sorted_population[0][1]}")

