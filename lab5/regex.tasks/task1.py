import re
with open(r"C:\Users\keeen\PycharmProjects\PythonProject\lab5\regex.tasks\row.txt", "r") as file:
    data = file.read()
x = re.findall(r"ab+", data)
y = re.findall(r"ab*", data)
print(x)
print(y)