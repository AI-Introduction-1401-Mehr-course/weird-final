from serializer import csp_from_io
from AC3 import AC_3
from sys import stdin
from datetime import timedelta, datetime
from copy import deepcopy

csp = csp_from_io(stdin)
start_time = datetime.now()
csp_copy = deepcopy(csp)
# backtracking(csp_copy)
runtime = datetime.now() - start_time
print("Runtime Without Using AC-3: " + str(runtime))

start_time = datetime.now()
ac3 = AC_3()
ac3(csp)
# backtracking(csp)
runtime = datetime.now() - start_time
print("Runtime When Using AC-3: " + str(runtime))
