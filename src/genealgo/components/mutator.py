from typing import Any, List
from abc import ABC, abstractmethod
import random


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
