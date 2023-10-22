#Task No 1(C)

my_tuple = (1, 2, 3, 4, "a", "abdullah")

# original tuple
print("Original Tuple:", my_tuple)


# length of the tuple 
length = len(my_tuple)
print("Length of the Tuple inside variable:", length)
my_tuple.__len__()
print("Length of the Tuple with function:", length)

# Access an item in the tuple using indexing
item = my_tuple[5]
print("Item at index 5:", item)

for item in my_tuple:
    print(item)
    
# Check if item exists in tuple
item_to_check = "abdullah"
if item_to_check in my_tuple:
    print("Item found in tuple")
else:
    print("Item not found in tuple")

