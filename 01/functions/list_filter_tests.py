from functions import *

# exponentiation tests
list1 = [1, 2, 3, 4, 5, 100, 101, 105]
list1_even = [2, 4, 100]
if list_filter(list1, FilterType.EVEN) != list1_even:
    print("Failed to filter list for even types")
    exit(1)

list1_odd = [1, 3, 5, 101, 105]
if list_filter(list1, FilterType.ODD) != list1_odd:
    print("Failed to filter list for odd types")
    exit(1)


list1_simple = [1, 2, 3, 5, 101]
if list_filter(list1, FilterType.SIMPLE) != list1_simple:
    print("Failed to filter list for simple types")
    exit(1)

print("All tests passed")