import math
from WeirdFinalCSP import WeirdFinalCSP
from safe_typing import Dict
from copy import deepcopy


class BackTrackingSearch:
    def search(self, csp: WeirdFinalCSP, assignments: Dict):
        if self.is_complete(csp, assignments):
            return assignments
        var = self.MRV(csp, assignments)
        if var == None:
            return None
        for val, _ in self.LCV(csp, var):
            assignments[var] = val
            fwd_csp = self.forwardChecking(csp, var, val)
            result = self.search(fwd_csp, assignments)
            if result != None:
                return result
            del assignments[var]

        return None

    def is_complete(self, csp: WeirdFinalCSP, assignments: Dict):
        return len(assignments) == csp.hall_count

    def MRV(self, csp: WeirdFinalCSP, assignments: Dict):
        mrv = None
        min_val = math.inf
        for var in range(csp.hall_count):
            if var in assignments:
                continue
            val_count = len(csp.hall_group_candidates[var])
            if val_count < min_val:
                min_val = val_count
                mrv = var

        return mrv

    def LCV(self, csp: WeirdFinalCSP, variable: int):
        lcv = []
        for val in csp.hall_group_candidates[variable]:
            constraints = 0
            for var in csp.hall_hall_exit_restrictions[variable]:
                if val in csp.hall_group_candidates[var]:
                    constraints += 1
            lcv.append((val, constraints))

        return sorted(lcv, key=lambda x: x[1])

    def forwardChecking(self, csp: WeirdFinalCSP, variable: int, value: int):
        new_csp = deepcopy(csp)
        for var in csp.hall_hall_exit_restrictions[variable]:
            new_group_candidate = []
            for val in csp.hall_group_candidates[var]:
                if val != value:
                    new_group_candidate.append(val)
            mutable_group_candidates = list(new_csp.hall_group_candidates)
            mutable_group_candidates[var] = new_group_candidate
            new_csp.hall_group_candidates = tuple(mutable_group_candidates)

        return new_csp
