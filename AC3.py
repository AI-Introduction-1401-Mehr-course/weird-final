from abstracts.algorithm import Algorithm
from WeirdFinalCSP import WeirdFinalCSP
from safe_typing import Dict


class AC_3(Algorithm):
    def __call__(
        self, csp: WeirdFinalCSP
    ) -> Dict[WeirdFinalCSP.Variable, WeirdFinalCSP.Value]:
        def revise(x: int, y: int, csp: WeirdFinalCSP):
            revised = False
            x_domain = csp.Domain()[x]
            y_domain = csp.Domain()[y]

            xy_constraints = [
                constraint
                for constraint in csp.Constraints()
                if constraint.scope[0] == x and constraint.scope[1] == y
            ] + [
                constraint
                for constraint in csp.Constraints()
                if constraint.scope[0] == y and constraint.scope[1] == x
            ]

            for x_value in x_domain:
                satisfies = False
                for y_value in y_domain:
                    for constraint in xy_constraints:
                        if (x_value, y_value) in constraint.relation:
                            satisfies = True
                if not satisfies:
                    x_domain.remove(x_value)
                    revised = True
            return revised

        arcs = [
            (constraint.scope[0], constraint.scope[1])
            for constraint in csp.Constraints()
        ] + [
            (constraint.scope[1], constraint.scope[0])
            for constraint in csp.Constraints()
        ]

        queue = arcs[:]
        while queue:
            (x, y) = queue.pop(0)
            revised = revise(x, y, csp)
            if revised:
                neighbors = [
                    neighbor
                    for neighbor in arcs
                    if neighbor[1] == x and neighbor not in queue
                ]
                queue = queue + neighbors
