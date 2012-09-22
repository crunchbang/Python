import string
import random
import math
from collections import namedtuple

Chromosome = namedtuple('Chromosome', ['code', 'cost'])

CHAR_POOL = string.ascii_letters + string.digits + string.punctuation + ' '

def get_cost(code, result):
	return sum(map(lambda x, y: math.pow(ord(x) - ord(y), 2), list(code), list(result.code)))

def crossover(parent1, parent2, chance, result):
	pivot = len(result.code) / 2
	#pivot = random.randint(1, len(result.code) - 1)
	#if chance > random.random():
	offspring1 = parent2.code[:pivot] + parent1.code[pivot:]
	offspring2 = parent1.code[:pivot] + parent2.code[pivot:]
	child1 = Chromosome(offspring1, get_cost(offspring1, result))
	child2 = Chromosome(offspring2, get_cost(offspring2, result))
	return child1, child2

def mutate(c1, chance, result):
	def upOrdown(a):
		return chr((ord(a) + random.choice([1, -1])) % 256)
	if chance > random.random():
		code = c1.code
		loc = random.randint(0, len(code) - 2)
		code = code[:loc] + upOrdown(code[loc]) + code[loc+1:]
		c1 = Chromosome(code, get_cost(code, result))
	return c1

def create_population(size, result):
	length = len(result.code)
	pop = []
	for x in range(size):
		code = ''.join(random.choice(CHAR_POOL) for i in range(length))
		candidate = Chromosome(code, get_cost(code, result))
		pop.append(candidate)
	return pop

if __name__ == "__main__":

	global_opt = Chromosome('Hello, World!', '0')
	mutation_chance = 0.3
	crossover_chance = 0.7
	pop_size = 20
	genepool = create_population(pop_size, global_opt)
	generation = 0
	while genepool[0].cost != 0:
		print genepool[0], ' ', generation
		genepool = genepool[:pop_size]
		rand_cand = random.choice(range(pop_size))
		genepool[rand_cand] = mutate(genepool[rand_cand], mutation_chance, global_opt)
		parent1, parent2 = random.sample(genepool, 2)
		child1, child2 = crossover(parent1, parent2, crossover_chance, global_opt)
		genepool.append(child1)
		genepool.append(child2)
		generation += 1
		genepool = sorted(genepool, key = lambda x: x.cost)
		#raw_input()

		

		
