import re
with open(r"C:\Users\keeen\PycharmProjects\PythonProject\lab5\regex.tasks\row.txt", "r") as file:
    data = file.read()
def snake_to_camel(snake_str):
    words = snake_str.split('_')
    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel_case_str
snake_str = data
camel_case_str = snake_to_camel(snake_str)
print("CamelCase String:", camel_case_str)
