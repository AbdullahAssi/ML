try:
    # Used "a" to append to the file
    with open("hello.txt", "a") as file:
        file.write("hi python programming\n")  

    print("Successfully added content to the file.")
except IOError as e:
    print(f"An error occurred: {e}")
