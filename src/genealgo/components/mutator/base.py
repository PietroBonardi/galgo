from typing import Any
from abc import ABC, abstractmethod


class Mutator(ABC):
    """
    A class responsible for applying mutations to individuals.

    Attributes:
        mutation_rate (float): The rate at which mutations occur.
    """

    def __init__(self, mutation_rate: float) -> None:
        """
        Initialize a Mutator with the given mutation rate.

        Args:
            mutation_rate (float): The rate at which mutations occur.
        """
        self._mutation_rate = mutation_rate

    def set_mutation_rate(self, value: float) -> None:
        """
        Set the mutation rate.

        Args:
            value (float): The new mutation rate.
        """
        self._mutation_rate = value

    def get_mutation_rate(self) -> float:
        """
        Get the current mutation rate.

        Returns:
            float: The current mutation rate.
        """
        return self._mutation_rate

    @abstractmethod
    def mutate(self, individual: Any) -> Any:
        """
        Apply a mutation to the given individual.

        Args:
            individual (Any): The individual to be mutated.

        Returns:
            Any: The mutated individual.

        Raises:
            NotImplementedError: This method should be overridden by subclasses.
        """
        raise NotImplementedError
