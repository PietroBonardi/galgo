from abc import ABC, abstractmethod
from typing import List, Tuple, Any


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
