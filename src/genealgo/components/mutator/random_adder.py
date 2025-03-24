from typing import Any, List
import random
from genealgo.components.mutator.base import Mutator


class RandomAdderMutator(Mutator):
    """
    A mutator that add random genes within a specified range.
    """

    def __init__(
        self, mutation_rate: float, characteristic: List[Any], max_genes: int = 5
    ):
        """
        Initialize the RandomResettingMutator with a mutation rate and value range.

        Args:
            mutation_rate (float): The probability of mutation.
            characteristic (List[Any]): The range of values for resetting genes.
        """
        super().__init__(mutation_rate)
        self.max_genes = max_genes
        self.characteristic = characteristic

    def mutate(self, offspring: List[Any]) -> List[Any]:
        """
        Mutate the offspring by resetting genes to random values within the specified range.

        Args:
            offspring (List[Any]): The offspring to be mutated.

        Returns:
            List[Any]: The mutated offspring.
        """
        genes_to_add = random.randint(1, self.max_genes)

        for _ in range(genes_to_add):
            if random.random() < self.get_mutation_rate():
                offspring.append(random.choice(self.characteristic))

        return offspring.copy()
