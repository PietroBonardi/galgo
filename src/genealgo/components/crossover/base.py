from abc import ABC, abstractmethod
from typing import Any, Tuple


class CrossOver(ABC):
    """
    A base class to represent a CrossOver operation for genetic algorithms.
    """

    @abstractmethod
    def __call__(self, X: Any, Y: Any) -> Tuple[Any, Any]:
        """
        Perform a crossover operation on two parents to produce two offspring.
        This method should be overridden by subclasses.

        Args:
            parent1 (Any): The first parent.
            parent2 (Any): The second parent.

        Returns:
            Tuple[Any, Any]: A tuple containing two offspring.
        """
        raise NotImplementedError("Subclasses should implement this method.")
