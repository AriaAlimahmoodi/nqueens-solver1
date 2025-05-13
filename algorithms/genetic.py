import random

class Genetic:
    def __init__(self, n, pop_size=200, generations=1000, mutation_rate=0.2):
        self.n = n
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate

    def fitness(self, board):
        n = len(board)
        diag1 = [0] * (2 * n)
        diag2 = [0] * (2 * n)
        conflicts = 0
        for i in range(n):
            diag1[i + board[i]] += 1
            diag2[i - board[i]] += 1
        for i in range(2 * n):
            if diag1[i] > 1:
                conflicts += diag1[i] * (diag1[i] - 1) // 2
            if diag2[i] > 1:
                conflicts += diag2[i] * (diag2[i] - 1) // 2
        return conflicts

    def generate_population(self):
        return [random.sample(range(self.n), self.n) for _ in range(self.pop_size)]

    def selection(self, population):
        return sorted(population, key=self.fitness)[:self.pop_size // 2]

    def crossover(self, parent1, parent2):
        # Order Crossover (OX)
        n = len(parent1)
        start, end = sorted(random.sample(range(n), 2))
        child = [-1] * n
        child[start:end] = parent1[start:end]
        pointer = end
        for gene in parent2:
            if gene not in child:
                if pointer >= n:
                    pointer = 0
                child[pointer] = gene
                pointer += 1
        return child

    def mutate(self, board):
        i, j = random.sample(range(self.n), 2)
        board[i], board[j] = board[j], board[i]
        return board

    def genetic_algorithm(self):
        population = self.generate_population()
        for gen in range(self.generations):
            population = self.selection(population)
            new_population = population[:]
            while len(new_population) < self.pop_size:
                parent1, parent2 = random.sample(population, 2)
                child = self.crossover(parent1, parent2)
                if random.random() < self.mutation_rate:
                    child = self.mutate(child)
                new_population.append(child)
            population = new_population
            for board in population:
                if self.fitness(board) == 0:
                    print(f"✅ Solution found in generation {gen}")
                    return board
        return None
