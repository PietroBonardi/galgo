from typing import Any, List
import random
from genealgo.components.mutator.base import Mutator

class SwapMutator(Mutator):
    """
    A mutator that swaps the positions of two randomly selected genes in the offspring.
    """

    def mutate(self, offspring: List[Any]) -> List[Any]:
        """
        Mutate the offspring by swapping the positions of two randomly selected genes.

        Args:
            offspring (List[Any]): The offspring to be mutated.

        Returns:
            List[Any]: The mutated offspring.
        """
        if random.random() < self.mutation_rate:
            # Ensure there are at least two genes to swap
            if len(offspring) < 2:
                return offspring
            # swap the genes
            idx1, idx2 = random.sample(range(len(offspring)), 2)
            offspring[idx1], offspring[idx2] = offspring[idx2], offspring[idx1]

        return offspring
