import os

def check_access(path):
    print("Path exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

path = input("Enter a path to check: ")
check_access(path)
