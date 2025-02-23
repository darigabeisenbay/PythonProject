import re
with open (r"C:\Users\keeen\PycharmProjects\PythonProject\lab5\regex.tasks\row.txt", "r") as file:
    data = file.read()
x = re.sub(r"[ ,.]", ":", data)
print(x)