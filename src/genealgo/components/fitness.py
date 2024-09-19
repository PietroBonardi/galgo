from abc import ABC, abstractmethod
import Levenshtein


class Fitness(ABC):
    """
    Abstract base class for fitness evaluation.
    """

    @abstractmethod
    def evaluate(self, individual) -> float:
        """
        Evaluate the fitness of an individual.

        Parameters:
        individual (Individual): The individual to evaluate.

        Returns:
        float: The fitness value of the individual.
        """
        raise NotImplementedError


class StringFitness(Fitness):

    def __init__(self, target_value: str) -> None:
        super().__init__()
        self.target_value = target_value

    def evaluate(self, individual: str) -> float:
        distance = Levenshtein.distance(self.target_value, individual)
        # Inverse to get a fitness
        return 1 / (distance + 1)
