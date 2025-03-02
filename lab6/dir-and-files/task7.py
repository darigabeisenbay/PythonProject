def copy_file(source, destination):
    try:
        with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
            dest.write(src.read())
        print(f"Copied contents from {source} to {destination}")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")
copy_file(source_file, destination_file)
