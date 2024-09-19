import random
from abc import ABC, abstractmethod
from typing import List, Tuple, Any
import pandas as pd


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

    def select(self, fitnesses: List[float], population: List[Any]) -> Tuple[Any, Any]:
        tot_fitness = sum(fitnesses)
        sel_proba = [score / tot_fitness for score in fitnesses]

        cond = True
        while cond:
            X = random.choices(population, sel_proba)[0]
            Y = random.choices(population, sel_proba)[0]
            cond = X == Y 
        
        return X, Y
