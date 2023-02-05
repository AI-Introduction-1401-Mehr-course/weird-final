from WeirdFinalCSP import WeirdFinalCSP
from serializer import csp_from_io
import sys
from BackTrack import BackTrackingSearch

csp: WeirdFinalCSP


def print_usage():
    print(" usage:")
    print("\tpython3", sys.argv[0], "path/to/problem_input.txt")


if len(sys.argv) != 2:
    print_usage()
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    csp = csp_from_io(f)

    bt = BackTrackingSearch()

    result = bt.search(csp, {})
    if result != None:
        for i in range(csp.hall_count):
            print(result[i] + 1, end=" ")
    else:
        print("No")
