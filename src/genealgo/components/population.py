from typing import List, Tuple
import random
import string


class StringPopulation:

    def __init__(
        self,
        pop_size: int = 10,
        individual_size: Tuple[int, int] = (1, 10),
    ) -> None:
        self._pop_size = pop_size
        self._ind_lb_size, self._ind_up_size = self.set_individual_size(individual_size)

    def set_individual_size(self, individual_size: Tuple[int, int]) -> Tuple[int, int]:
        lb, up = individual_size
        assert (
            lb > 0 and up > 0 and lb < up + 1
        ), f"😵‍💫 Invalid size range: ({lb}, {up})"

        return lb, up + 1

    def generate_population(
        self,
    ) -> List[str]:
        return [self.generate_individual() for _ in range(self._pop_size)]

    def generate_individual(self) -> str:
        return "".join(
            random.choice(string.ascii_lowercase)
            for _ in range(random.choice(range(self._ind_lb_size, self._ind_up_size)))
        )