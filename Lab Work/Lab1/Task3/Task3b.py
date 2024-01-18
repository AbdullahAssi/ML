#Task no 3(B)
print("Palindrome String Example \n \n racecar ")

def is_palindrome(s):
    # Removing spaces and converting to lowercase to make the check case-insensitive and space-insensitive
    s = s.replace(" ", "").lower()
    
    # Comparing the original string with its reverse
    return s == s[::-1]

# Input string
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
