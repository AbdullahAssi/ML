#Task No 4(D)
from functools import reduce

my_list = [1, 2, 3, 4, 5]

# Using reduce() to find the sum of the numbers in the list
sum_of_numbers = reduce(lambda x, y: x + y, my_list)

print("The list is:", my_list)
print("The sum of the numbers in the list is:", sum_of_numbers)
