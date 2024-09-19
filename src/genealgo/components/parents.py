from abc import ABC, abstractmethod
from typing import List, Tuple, Any
import random


class ParentSelector(ABC):
    """
    Abstract base class for parent selection strategies.
    """

    @abstractmethod
    def select(self, population: List[Any], fitnesses: List[float]) -> Tuple[Any, Any]:
        """
        Select two parents from the population based on fitness scores.

        Parameters:
        population (list): List of individuals in the population.
        fitness_scores (list): List of fitness scores corresponding to the individuals.

        Returns:
        tuple: Two selected parents.
        """
        raise NotImplementedError


class RouletteWheelSelector(ParentSelector):
    """
    Roulette Wheel Selector for genetic algorithms.

    This class implements a selection method based on roulette wheel selection,
    where individuals are selected proportionally to their fitness scores.
    """

    def select(self, fitnesses: List[float], population: List[Any]) -> Tuple[Any, Any]:
        """
        Selects two distinct individuals from the population based on their fitness scores.

        This method uses the roulette wheel selection algorithm, where the probability of
        selecting an individual is proportional to its fitness score. It ensures that the
        two selected individuals are distinct.

        Args:
            fitnesses (List[float]): A list of fitness scores corresponding to the individuals
                in the population.
            population (List[Any]): A list of individuals in the population.

        Returns:
            Tuple[Any, Any]: A tuple containing two distinct individuals selected from the
                population.
        """
        tot_fitness = sum(fitnesses)
        sel_proba = [score / tot_fitness for score in fitnesses]

        cond = True
        while cond:
            X = random.choices(population, sel_proba)[0]
            Y = random.choices(population, sel_proba)[0]
            cond = X == Y

        return X, Y
