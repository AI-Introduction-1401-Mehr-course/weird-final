from functools import cache
from abstracts import CSP
from safe_typing import Tuple, Iterable, List


class WeirdFinalCSP(CSP):
    hall_count: int
    group_count: int
    hall_group_candidates: Tuple[List[int]]
    hall_hall_exit_restrictions: Tuple[List[int]]

    def __init__(
        self,
        hall_count: int,
        group_count: int,
        hall_group_candidates: Tuple[List[int]],
        hall_hall_exit_restrictions: Tuple[List[int]],
    ):
        super().__init__()
        self.hall_count = hall_count
        self.group_count = group_count
        self.hall_group_candidates = hall_group_candidates
        self.hall_hall_exit_restrictions = hall_hall_exit_restrictions

    def X(self):
        return tuple(range(self.hall_count))

    def Domain(self):
        return self.hall_group_candidates

    @cache
    def Constraints(self) -> Tuple[CSP.Constraint]:
        class HallExitRestriction(CSP.Relation):
            problem = self

            def __init__(self, from_hall: int, to_hall: int) -> None:
                self.from_hall = from_hall
                self.to_hall = to_hall

            def __contains__(self, groups: Tuple[int, int]):
                return groups[0] != groups[1]

            def __iter__(self):
                for i in self.problem.hall_group_candidates[self.from_hall]:
                    for j in self.problem.hall_group_candidates[self.to_hall]:
                        if i != j:
                            yield (i, j)

        constraints = tuple()

        for i in range(self.hall_count):
            constraints += tuple(
                ((i, j), HallExitRestriction(i, j))
                for j in self.hall_hall_exit_restrictions[i]
            )

        return constraints
