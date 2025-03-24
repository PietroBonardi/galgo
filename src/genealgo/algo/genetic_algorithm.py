from typing import Any, List, Tuple
from genealgo.components.fitness import Fitness
from genealgo.components.parent.roulette_wheel import ParentSelector
from genealgo.components.mutator.base import Mutator
from genealgo.components.crossover.base import CrossOver


class GeneticAlgo:
    """
    A class to represent a genetic algorithm.

    Attributes:
        fitness (Fitness): The fitness evaluation component.
        parent_selector (ParentSelector): The parent selection component.
        mutator (Mutator): The mutation component.
        crossover (CrossOver): The crossover component.
        generations (int): The number of generations to run the algorithm.
    """

    def __init__(
        self,
        fitness: Fitness,
        parent_selector: ParentSelector,
        mutator: Mutator,
        crossover: CrossOver,
        generations: int = 10,
    ) -> None:
        """
        Initialize the GeneticAlgo class with the specified components.

        Args:
            fitness (Fitness): The fitness evaluation component.
            parent_selector (ParentSelector): The parent selection component.
            mutator (Mutator): The mutation component.
            crossover (CrossOver): The crossover component.
            generations (int): The number of generations to run the algorithm. Default is 10.
        """
        self.fitness = fitness
        self.parent_selector = parent_selector
        self.crossover = crossover
        self.mutator = mutator
        self.generations = generations

    def compute_fitness(self, population: List[Any]) -> List[float]:
        """
        Compute the fitness of each individual in the population.

        Args:
            population (List[Any]): The population of individuals.

        Returns:
            List[float]: A list of fitness values corresponding to the individuals.
        """
        return [self.fitness.evaluate(individual) for individual in population]

    def select_parents(
        self, population: List[Any], fitnesses: List[float]
    ) -> Tuple[Any, Any]:
        """
        Select two parents from the population based on their fitnesses.

        Args:
            population (List[Any]): The population of individuals.
            fitnesses (List[float]): The fitness values of the individuals.

        Returns:
            Tuple[Any, Any]: A tuple containing two selected parents.
        """
        return self.parent_selector.select(population=population, fitnesses=fitnesses)

    def best_gene(self, population: List[Any]) -> Tuple[Any, float]:
        """
        Find the best individual in the population based on fitness.

        Args:
            population (List[Any]): The population of individuals.
            fitnesses (List[float]): The fitness values of the individuals.

        Returns:
            Tuple[Any, float]: A tuple containing the best individual and its fitness.
        """
        fit_pop = zip(population, self.compute_fitness(population))
        return sorted(list(fit_pop), key=lambda x: x[1])[-1]

    def __call__(self, population: List[Any]) -> List[str]:
        """
        Run the genetic algorithm for the specified number of generations.

        Args:
            population (List[Any]): The initial population of individuals.

        Returns:
            List[str]: A list of the best individuals from each generation as strings.
        """
        best_genes = []

        for _ in range(self.generations):
            fitnesses = self.compute_fitness(population)
            new_pop = []
            for _ in range(len(population) // 2):
                # Select parents
                X, Y = self.select_parents(population, fitnesses)
                # Perform crossover
                offspringX, offspringY = self.crossover(X, Y)
                # Apply mutation
                offspringX = self.mutator.mutate(offspringX)
                offspringY = self.mutator.mutate(offspringY)
                # Add offspring to the new population
                new_pop.extend([offspringX, offspringY])

            population = new_pop
            best_genes.append(self.best_gene(population))

            # Early stop condition
            if best_genes[-1][1] == 1:
                return [ind for ind, _ in best_genes]

        return [ind for ind, _ in best_genes]
