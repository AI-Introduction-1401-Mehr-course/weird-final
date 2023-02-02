from abc import ABC, abstractmethod
from safe_typing import Tuple, Iterable


class CSP(ABC):

    Variable = str | int
    Value = int
    Scope = Tuple[Variable, ...]
    Relation = Iterable[Value]
    Constraint = Tuple[Scope, Relation]

    @abstractmethod
    def X(self) -> Tuple[Variable]:
        ...

    @abstractmethod
    def Domain(self) -> Tuple[Iterable]:
        ...

    @abstractmethod
    def Constraints(self) -> Tuple[Constraint]:
        ...
