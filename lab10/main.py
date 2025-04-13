import csv

import psycopg2
from lab10.config import host, user, password, db_name

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True


    while True:
        q = input("2.1 inserting data from csv file \n"
                  "2.2 inserting data from console \n"
                  "3 updating name and number by id \n"
                  "4.1 filtering by name \n"
                  "4.2  filtering by number \n"
                  "5 deleting data by username \n"
                  "6 to quit \n"
                  "ENTER A NUMBER:\n")
        if q == "2.1":
            # 2.1 insert from csv file
            with open("phonebook.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                with connection.cursor() as cursor:
                    for row in reader:
                        cursor.execute(
                            "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s);",
                            (row['name'], row['phone'])
                        )
                    print("CSV data inserted!")

        elif q == "2.2":
            # 2.2 insert from console
            n = input("Enter name: ")
            p = input("Enter phone: ")
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s);",
                    (n, p)
                )
                print("Data inserted successfully!")
        elif q == "3":
            # 3 update name and number by id
            user_id = input("Введите ID пользователя, которого хотите обновить: ")
            new_name = input("Введите новое имя: ")
            new_phone = input("Введите новый номер телефона: ")

            with connection.cursor() as cursor:
                cursor.execute(
                "UPDATE PhoneBook SET name = %s, phone = %s WHERE id = %s;",
                (new_name, new_phone, user_id)
                )
            connection.commit()
            print("Имя и номер успешно обновлены!")
        elif q == "4.1":
            # 4.1 filter by name
            a = input("Введите первые буквы имени: ")
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM PhoneBook WHERE name LIKE %s;",
                    (a + '%',)
                )
                results1 = cursor.fetchall()  # теперь курсор еще активен
                for row in results1:
                    print(row)

        elif q == "4.2":
            # 4.2 filter by number
            a = input("Введите часть номера: ")
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM PhoneBook WHERE phone like %s;",
                    ('%' + a + '%',)
                )
                results2 = cursor.fetchall()
                for row in results2:
                    print(row)
        elif q == "5":
            # 5 deleting by username
            username = input("Enter username: ")
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM PhoneBook WHERE name = %s;",
                    (username,)
                )
                print(f"{username} has been deleted")
        elif q == "6":
            quit()

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
