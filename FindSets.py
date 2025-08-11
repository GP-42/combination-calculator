from itertools import combinations

def find_sets(numbers_per_set, total_per_set=0, min_number=1, max_number=9):
    """
    Find all sets of numbers between min_number and max_number (incl.) where the amount of numbers per set equals
    'numbers_per_set'. If 'total_per_set' is provided, only sets with a sum matching 'total_per_set' are returned.
    Every set is returned as a tuple (set, total).
    If 'sum' is out of range of the possible sums, 2 sets are returned: a set with the minimum sum and a set with
    the maximum sum.

    :param numbers_per_set: Amount of numbers per set
    :param total_per_set: Expected sum of the numbers in the set (by default 0)
    :param min_number: Minimum number in range (by default 1)
    :param max_number: Maximum number in range (by default 9)
    :return: List of tuples (set, total)
    """
    numbers = range(min_number, max_number + 1)
    sets = []

    for combination in combinations(numbers, numbers_per_set):
        total = sum(combination)
        if total_per_set == 0 or total == total_per_set:
            sets.append((combination, total))

    if not sets and total != 0:
        # Minimum sum
        min_combination = tuple(sorted(numbers[:numbers_per_set]))
        min_total = sum(min_combination)
        sets.append((min_combination, min_total))
        
        # Maximum sum
        max_combination = tuple(sorted(numbers[-numbers_per_set:]))
        max_total = sum(max_combination)
        sets.append((max_combination, max_total))

    return sets

"""
TESTING CODE 1

print("All sets of 2")
my_sets = find_sets(2)
for my_set, total in my_sets:
    print(f"{my_set} = {total}")

print("All sets of 2 with a sum of 11")
my_sets = find_sets(2, 11)
for my_set, total in my_sets:
    print(f"{my_set} = {total}")

print("All sets of 2 with a sum of 25")
my_sets = find_sets(2, 25)
for my_set, total in my_sets:
    print(f"{my_set} = {total}")

TESTING CODE 2

import pprint

number_of_rows = 45
number_of_cols = 9
matrix = [[False for col in range(number_of_cols)] for row in range(number_of_rows)]
pprint.pp(matrix)

#matrix[3][2] = True
#print(matrix)

my_sets = find_sets(2)
for my_set, total in my_sets:
    print(f"{my_set} = {total}")
    row_index = total-1
    for item in my_set:
        col_index = item-1
        matrix[row_index][col_index] = True

pprint.pp(matrix)
"""