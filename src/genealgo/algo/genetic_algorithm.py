from typing import Any, List, Tuple
from genealgo.components.fitness import Fitness
from genealgo.components.parents import ParentSelector
import random
import string


class GeneticAlgo:

    def __init__(
        self,
        fitness: Fitness,
        parent_selector: ParentSelector,
        generation: int = 1,
        mutation_rate: float = 0.01,
    ) -> None:
        self.fitness = fitness
        self.parent_selector = parent_selector
        self.generation = generation
        self.mutation_rate = mutation_rate

    def compute_fitness(self, population: List[Any]) -> List[float]:
        return [self.fitness.evaluate(individual) for individual in population]

    def select_parents(
        self, population: List[Any], fitnesses: List[float]
    ) -> Tuple[Any, Any]:
        return self.parent_selector.select(population=population, fitnesses=fitnesses)

    def crossover(self, X: Any, Y: Any) -> Tuple[Any, Any]: # TODO: Class
        crossover_point = min(len(X) // 2, len(Y) // 2)
        offspringX = X[:crossover_point] + Y[crossover_point:]
        offspringY = Y[:crossover_point] + X[crossover_point:]

        return offspringX, offspringY

    def mutate(self, offspring: Any) -> Any: # TODO: Class
        mutation = []
        for i in range(len(offspring)):
            if random.random() < self.mutation_rate:
                mutation.append(random.choice(string.ascii_lowercase))
            else:
                mutation.append(offspring[i])
        return "".join(mutation)

    def __call__(self, population) -> Any:
        for _ in range(self.generation): 
            fitnesses = self.compute_fitness(population)

            new_pop = []
            for _ in range(len(population) // 2):
                # selection
                X, Y = self.select_parents(population, fitnesses)
                # cross-over
                offspringX, offspringY = self.crossover(X, Y)
                # mutation
                offspringX = self.mutate(offspringX)
                offspringY = self.mutate(offspringY)
                new_pop.extend([offspringX, offspringY])

            population = new_pop

        max_ = -1
        best = ""
        for ind, score in zip(population, self.compute_fitness(population)):
            if score > max_:
                max_ = score
                best = ind

        return best
