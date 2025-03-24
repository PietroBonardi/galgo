from abc import ABC, abstractmethod
from typing import Any, List

class Fitness(ABC):
    """
    Abstract base class for fitness evaluation.
    """

    @abstractmethod
    def evaluate(self, individual:List[Any]) -> float:
        """
        Evaluate the fitness of an individual.

        Parameters:
            individual (Individual): The individual to evaluate.

        Returns:
            float: The fitness value of the individual.
        """
        raise NotImplementedError