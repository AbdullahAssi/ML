#Task No 3(A)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

print("The menu is given below:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Exit")

input_num = int(input("Enter your choice: "))

if input_num == 5:
    print("\nExit")
elif input_num in (1, 2, 3, 4):
    num_1 = float(input("\nEnter the first number: "))
    num_2 = float(input("Enter the second number: "))

    if input_num == 1:
        result = add(num_1, num_2)
    elif input_num == 2:
        result = subtract(num_1, num_2)
    elif input_num == 3:
        result = multiply(num_1, num_2)
    elif input_num == 4:
        result = divide(num_1, num_2)

    print("Result:", result)
else:
    print("Invalid choice. Please choose a valid option.")
