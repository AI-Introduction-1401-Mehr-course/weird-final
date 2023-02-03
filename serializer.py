from WeirdFinalCSP import WeirdFinalCSP
from safe_typing import IO


def csp_from_io(io: IO[str]):
    hall_count, group_count = (int(i) for i in next(io).split())

    hall_group_candidates = tuple([] for _ in range(hall_count))
    for i in range(group_count):
        for j in (int(i) for i in next(io).split()):
            hall_group_candidates[j - 1].append(i)

    hall_hall_exit_restrictions = tuple([] for _ in range(hall_count))
    for i in range(int(next(io))):
        from_hall, to_hall = (int(j) - 1 for j in next(io).split())
        hall_hall_exit_restrictions[from_hall].append(to_hall)

    return WeirdFinalCSP(hall_count, hall_group_candidates, hall_hall_exit_restrictions)
