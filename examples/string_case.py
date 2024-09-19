from genealgo.components.population import Population
from genealgo.components.fitness import Fitness

from typing import Tuple
import Levenshtein
import string
import random


class StringPopulation(Population):
    def __init__(
        self,
        pop_size: int = 10,
        individual_size: Tuple[int, int] = (1, 10),
    ) -> None:
        super.__init__(pop_size)
        self._ind_lb_size, self._ind_up_size = self.set_individual_size(individual_size)

    def set_individual_size(self, individual_size: Tuple[int, int]) -> Tuple[int, int]:
        lb, up = individual_size
        assert (
            lb > 0 and up > 0 and lb < up + 1
        ), f"😵‍💫 Invalid size range: ({lb}, {up})"

        return lb, up + 1

    def generate_individual(self) -> str:
        return "".join(
            random.choice(string.ascii_lowercase)
            for _ in range(random.choice(range(self._ind_lb_size, self._ind_up_size)))
        )


class StringFitness(Fitness):

    def __init__(self, target_value: str) -> None:
        super().__init__()
        self.target_value = target_value

    def evaluate(self, individual: str) -> float:
        distance = Levenshtein.distance(self.target_value, individual)
        # Inverse to get a fitness
        return 1 / (distance + 1)
