import random
from abc import ABC, abstractmethod
from typing import Any, List, Tuple


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


class SinglePointCrossOver(CrossOver):
    """
    A class to represent a Single-Point CrossOver operation for genetic algorithms.
    """

    def __init__(self, op_mod="balance") -> None:
        self._op_mod = op_mod

    def __call__(self, X: List[Any], Y: List[Any]) -> Tuple[List[Any], List[Any]]:
        """
        Perform a single-point crossover operation on two parents to produce two offspring.

        Args:
            parent1 (List[Any]): The first parent.
            parent2 (List[Any]): The second parent.

        Returns:
            Tuple[List[Any], List[Any]]: A tuple containing two offspring.
        """
        crossover_point = {
            "min": min(len(X), len(Y)),
            "balance": min(len(X) // 2, len(Y) // 2),
        }[self._op_mod]

        X_mod = X[:crossover_point] + Y[crossover_point:]
        Y_mod = Y[:crossover_point] + X[crossover_point:]

        return X_mod, Y_mod