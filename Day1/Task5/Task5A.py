import sys

try:
    # x = 1 / 0
    print("Hello from Try Block")
except Exception as e:
    print("An error occurred:", e)
    sys.exit(0) 

print("This code will not be executed if an exception occurs")
