from abc import ABC, abstractmethod
from safe_typing import Tuple, Iterable, NamedTuple


class CSP(ABC):

    Variable = int
    Value = int
    Scope = Tuple[Variable, ...]
    Relation = Iterable[Tuple[Value, ...]]

    class Constraint(NamedTuple):
        scope: "CSP.Scope"
        relation: "CSP.Relation"

    @abstractmethod
    def X(self) -> Tuple[Variable]:
        ...

    @abstractmethod
    def Domain(self) -> Tuple[Iterable]:
        ...

    @abstractmethod
    def Constraints(self) -> Tuple[Constraint]:
        ...
