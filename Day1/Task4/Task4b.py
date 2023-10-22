#Task No 4(B)
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = list(filter(is_even, numbers))


print("Even Numbers: ", even_numbers)

#lambda approach to filter
print("Odd Numbers: ", list(filter(lambda number: not is_even(number), numbers)))

