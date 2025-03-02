def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return len(file.readlines())
    except FileNotFoundError:
        print("File not found.")
        return None

file_path = input("Enter the file path: ")
lines = count_lines(file_path)
if lines is not None:
    print("Number of lines:", lines)
