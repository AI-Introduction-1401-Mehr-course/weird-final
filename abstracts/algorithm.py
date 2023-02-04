from abc import ABC, abstractmethod
from safe_typing import Dict
from .CSP import CSP


class Algorithm(ABC):
    @abstractmethod
    def __call__(self, csp: CSP) -> Dict[CSP.Variable, CSP.Value]:
        ...
