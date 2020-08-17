from functions import *

# exponentiation tests
list1 = [1, 2, 3, 4, 5]
list1_power_by_2 = [1, 4, 9, 16, 25]
if exponentiation(list1) != list1_power_by_2:
    print("Failed to power 'list1' of 2")
    exit(1)

list2 = [1, 2, 3, 4, 5]
list2_power_by_3 = [1, 8, 27, 64, 125]
if exponentiation(list2, 3) != list2_power_by_3:
    print("Failed to power 'list1' of 3")
    exit(1)

print("All tests passed")