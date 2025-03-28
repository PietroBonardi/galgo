from typing import List, Any
from abc import ABC, abstractmethod


class Population(ABC):
    """
    Represents a population of individuals.

    Attributes:
        _pop_size (int): The size of the population.
    """

    def __init__(self, pop_size: int) -> None:
        """
        Initialize a Population with the given size.

        Args:
            pop_size (int): The size of the population.
        """
        self._pop_size = pop_size

    @abstractmethod
    def generate_individual(self):
        """
        Generate an individual.

        Raises:
            NotImplementedError: This method should be overridden by subclasses.
        """
        raise NotImplementedError

    def generate(self) -> List[Any]:
        """
        Generate a population of individuals.

        Returns:
            List[str]: A list of generated individuals.

        Raises:
            AssertionError: If the population size is not greater than 0.
        """
        assert self._pop_size > 0, "Population size has to be greater than 0"
        return [self.generate_individual() for _ in range(self._pop_size)]
