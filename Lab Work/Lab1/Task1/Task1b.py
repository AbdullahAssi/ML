#Task No 1(B)

my_dict = {
    "Python": "Mango",
    "JS": "React", 
    "Java": "Spring",
    "C++": ""
}

#raw dictionary
print("Raw Dictionary:", my_dict)

#dictionary items as key-value pairs
print("Dictionary Items:", my_dict.items())

# dictionary keys
print("Dictionary Keys:", my_dict.keys())

#  dictionary values
print("Dictionary Values:", my_dict.values())

# length of the dictionary
print("Dictionary Length:", len(my_dict))

# Access an item in the dictionary using a key
print("Dictionary access items:", my_dict["Python"])

# Remove an item from the dictionary using pop
my_dict.pop("Python")
print("Dictionary after pop:", my_dict)

# Use get() to access an item with a default value if the key doesn't exist
my_dict.get("python", "Not Found")
print("Using get():", my_dict)

# Change the value associated with a key in the dictionary
my_dict["Python"] = "Django"
print("Modified Dictionary:", my_dict)
print("Fun Fact Dictionary seems the sister of JSON")
