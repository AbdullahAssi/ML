#Task No 1(A)

my_list = [1, 2, 'h', 4, "Abdullah"]
print( "Raw List =" , my_list)

my_list.insert(6,"Zafar")  # Insert "Zafar" at index 6
print("List after inserting" ,my_list)

my_list.remove('h')  # Remove the value 'h' from the list
print("List after removing ",my_list)


my_list.pop(2) # Remove the value at index 2
print("List after poping ",my_list)

my_list.__len__() # Get the length of the list
print("Length of the list is ",my_list.__len__())

my_list.clear() # Clear the list
print("List after clearing ",my_list)

