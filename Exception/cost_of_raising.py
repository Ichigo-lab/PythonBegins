# Raising is costly so prefer not raising exception
from timeit import timeit

cost1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10/age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

cost2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("Cost1: ", timeit(cost1, number=10000))
print("Cost2: ", timeit(cost2, number=10000))
