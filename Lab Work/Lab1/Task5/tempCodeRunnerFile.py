try:
    #"w" to write on a file
    with open("hello.txt", "w") as file:
        file.write("Hello, world\n")
    print("Successfully wrote 'Hello, world' to the file.")
except IOError as e:
    print(f"An error occurred: {e}")
