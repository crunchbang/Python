# genetic_algorithm.py

import string
import random
import math
from collections import namedtuple
import matplotlib.pyplot as plt#


# Each chromosome in a Gene pool is represented as a named
# tuple with attributes code(for storing the genetic code)
# and cost(to store the associated cost)
Chromosome = namedtuple('Chromosome', ['code', 'cost'])

# Possible letters for generating the chromosome
CHAR_POOL = string.ascii_letters + string.digits + string.punctuation + ' '

def isvalid(c):
	"""
	Checks if a chromosome is valid
	Args:
	    c : chromosome from genepool
	Returns:
	    True or False 
	"""
	return True if c.cost >= 0 else False
def get_cost(code, result):
	"""
	Calculate the cost of code.
	Cost is calculated by squaring the difference of ascii values 
	between two characters.
	Args:
	    code   : chromosome from genepool
	    result : the target chromosome
	Returns:
	    sum of costs associated with each character of code
	"""
	return sum(map(lambda x, y: math.pow(ord(x) - ord(y), 2), list(code), list(result.code)))

def crossover(parent1, parent2, chance, result):
	"""
	Crossover two chromosomes.
	Args:
	    parent1: chromosome from genepool
	    parent2: chromosome from genepool
	    chance : the probability the the parents will perform a cross over
	    result : the target chromosome
	Returns:
	    two children formed by combining parts of the parents
	"""
	pivot = len(result.code) / 2
	#pivot = random.randint(1, len(result.code) - 1)
	child1 = child2 = Chromosome('', -1)
	if chance > random.random():
		offspring1 = parent2.code[:pivot] + parent1.code[pivot:]
		offspring2 = parent1.code[:pivot] + parent2.code[pivot:]
		child1 = Chromosome(offspring1, get_cost(offspring1, result))
		child2 = Chromosome(offspring2, get_cost(offspring2, result))
	return child1, child2

def mutate(c1, chance, result):
	"""
	Mutates a chromosome by randomly incrementing or
	decrementing a character in it's code.
	Args:
	    c1     : chromosome from genepool
	    chance : probability that the chromosome will mutate
	    result : the target chromosome
	Returns:
	    mutated chromosome
	"""
	def upOrdown(a):
		"""
		flips a character by either incrementing or
		decrementing it's ascii value (0-255)
		"""
		return chr((ord(a) + random.choice([1, -1])) % 256)
	if chance > random.random():
		code = c1.code
		loc = random.randint(0, len(code) - 1)
		code = code[:loc] + upOrdown(code[loc]) + code[loc+1:]
		c1 = Chromosome(code, get_cost(code, result))
	return c1

def create_population(size, result):
	"""
	Creates a population of chromosomes
	Args:
	    size   : size of the population
	    result : the target chromosome
	Returns:
	    a population of chromosomes each having length equal to 'result'
	    and made up of random character
	"""
	length = len(result.code)
	pop = []
	for x in range(size):
		code = ''.join(random.choice(CHAR_POOL) for i in range(length))
		candidate = Chromosome(code, get_cost(code, result))
		pop.append(candidate)
	return pop

if __name__ == "__main__":
	global_opt = Chromosome("Hello, World!", 0) # The target chromosome
	crossover_chance = 0.7
	mutation_chance = 0.4
	pop_size = 20
	genepool = create_population(pop_size, global_opt)
	limit = 100000				    # The generation limit
	generation = 0
	scores = []
	gener = []
	avg = 0
	while genepool[0] != global_opt and generation < limit:
		print genepool[0], ' ', generation
		avg = sum([x.cost for x in genepool]) / pop_size#
		scores.append(avg)#
		gener.append(generation)#
		genepool = genepool[:pop_size]      # Maintain the population size; Kill the weak chromosomes
		rand_cand = random.choice(range(pop_size))
		genepool[rand_cand] = mutate(genepool[rand_cand], 
				mutation_chance, global_opt) # Randomly select individual for mutation
		parent1, parent2 = random.sample(genepool, 2)    # Randomly select parents from genepool
		child1, child2 = crossover(parent1, parent2, crossover_chance, global_opt)
		if isvalid(child1) and isvalid(child2):
			genepool.append(child1)
			genepool.append(child2)
		generation += 1
		genepool = sorted(genepool, key = lambda x: x.cost) # Sort genepool according to cost;From least to greatest
	print 'At generation:', generation, ': ', genepool[0]
	print 'Probability of mutation:', mutation_chance
	print 'Probability of crossover:', crossover_chance

	plt.plot(gener,scores)
	plt.ylabel("Avg cost per generation")
	plt.xlabel("Generation")
	plt.show()
