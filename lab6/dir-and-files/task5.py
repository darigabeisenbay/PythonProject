def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print("List written to file successfully.")
    except Exception as e:
        print("An error occurred:", e)

file_path = input("Enter the file path: ")
data_list = ["Apple", "Banana", "Cherry", "Date"]
write_list_to_file(file_path, data_list)
