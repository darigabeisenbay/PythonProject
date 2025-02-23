import re
with open (r"C:\Users\keeen\PycharmProjects\PythonProject\lab5\regex.tasks\row.txt", "r") as file:
    data = file.read()
def camel_to_snake(camel_str):
    result = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return result
camel_str = data
snake_case_str = camel_to_snake(camel_str)
print("Snake Case String:", snake_case_str)