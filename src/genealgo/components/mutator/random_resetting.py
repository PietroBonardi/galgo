from typing import Any, List
import random
from genealgo.components.mutator.base import Mutator


class RandomResettingMutator(Mutator):
    """
    A mutator that resets genes to random values within a specified range.
    """

    def __init__(self, mutation_rate: float, characteristics: List[Any]):
        """
        Initialize the RandomResettingMutator with a mutation rate and value range.

        Args:
            mutation_rate (float): The probability of mutation for each gene.
            characteristics (List[Any]): The range of values for resetting genes.
        """
        super().__init__(mutation_rate)
        self.characteristics = characteristics

    def mutate(self, offspring: List[Any]) -> List[Any]:
        """
        Mutate the offspring by resetting genes to random values within the specified range.

        Args:
            offspring (List[Any]): The offspring to be mutated.

        Returns:
            List[Any]: The mutated offspring.
        """
        for i in range(len(offspring)):
            if random.random() < self.get_mutation_rate():
                offspring[i] = random.choice(self.characteristics)

        return offspring.copy()
