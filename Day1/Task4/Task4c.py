#Task No 4(C)
def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]
#mapping the double function to the numbers list
doubles = map(double, numbers)

print("Original numbers:", numbers)
print("Doubles:", list(doubles))
