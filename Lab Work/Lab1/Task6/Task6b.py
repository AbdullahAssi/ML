import os

file_path = "hello.txt"

if os.access(file_path, os.R_OK):
    print(f"{file_path} has read access.")
else:
    print(f"{file_path} does not have read access.")

if os.access(file_path, os.W_OK):
    print(f"{file_path} has write access.")
else:
    print(f"{file_path} does not have write access.")


if os.access(file_path, os.X_OK):
    print(f"{file_path} is executable.")
else:
    print(f"{file_path} is not executable.")
