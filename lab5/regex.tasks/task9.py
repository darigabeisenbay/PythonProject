import re
with open (r"C:\Users\keeen\PycharmProjects\PythonProject\lab5\regex.tasks\row.txt", "r") as file:
    data = file.read()
def insert_spaces(s):
    result = re.sub(r'([A-Z])', r'\1 ', s).strip()
    return result
input_str = data
output_str = insert_spaces(input_str)
print("Modified String:", output_str)
