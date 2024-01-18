#Task no 4(A)
# Defining lambda functions 
double = lambda x: x * 2
add = lambda x, y: x + y

num = float(input("Enter a number: "))

doubled_num = double(num)
result = add(num, 2)

print(f"Double of {num} is {doubled_num}")
print(f"{num} + 2 = {result}")
