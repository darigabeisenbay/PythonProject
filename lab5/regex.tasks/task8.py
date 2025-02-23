import re
with open (r"C:\Users\keeen\PycharmProjects\PythonProject\lab5\regex.tasks\row.txt", "r") as file:
    data = file.read()
def split_at_uppercase(s):
    result = re.split(r'(?=[A-Z])', s)
    return result
input_str = data
split_str = split_at_uppercase(input_str)
print("Splitted String:", split_str)
