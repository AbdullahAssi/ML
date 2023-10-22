#Task No 3(C)
def factorial (n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


num = int(input("Enter a number to find a factorial: "))

if num<0:
    print("Factorial does not exist for negative numbers")
else:
    print("Factorial of", num, "is", factorial(num))