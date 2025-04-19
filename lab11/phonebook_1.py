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

    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS PhoneBook (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                surname TEXT NOT NULL,
                phone TEXT NOT NULL
            );
        """)
        print("[INFO] Table 'PhoneBook' created successfully")

    while True:
        q = input("Choose the function:\n"
                      "1 returning based on pattern\n"
                      "2 creating new user\n"
                      "3 creating users by list\n"
                      "4 pagination\n"
                      "5 deleting\n"
                      "6 to exit\n")


        def return_by_pattern():
            pattern = input("Enter a pattern: ")
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT * FROM PhoneBook
                    WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s
                """, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
                results = cursor.fetchall()
                for row in results:
                    print(row)


        def insert_or_update_user(name, surname, phone):
            with connection.cursor() as cursor:
                cursor.execute("CALL insert_or_update_user(%s, %s, %s);", (name, surname, phone))
                print(f"[INFO] User {name} {surname} inserted or updated")


        def get_paginated_data(limit_count, offset_count):
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM get_paginated_data(%s, %s)", (limit_count, offset_count))
                results = cursor.fetchall()
                for row in results:
                    print(row)



        if q == "1":
            return_by_pattern()
        elif q == "2":
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            phone = input("Enter phone: ")
            insert_or_update_user(name, surname, phone)

        elif q == "3":
            def get_user_data():
                names = []
                surnames = []
                phones = []
                while True:
                    name = input("Enter name (or 'done' to finish): ")
                    if name.lower() == 'done':
                        break
                    surname = input("Enter surname: ")
                    phone = input("Enter phone: ")

                    names.append(name)
                    surnames.append(surname)
                    phones.append(phone)

                return names, surnames, phones


            names, surnames, phones = get_user_data()  # Вводим данные через консоль
            with connection.cursor() as cursor:
                # Преобразуем данные в массивы строк
                names_array = names  # Это уже список строк
                surnames_array = surnames  # Это уже список строк
                phones_array = phones  # Это уже список строк

                # Вызов процедуры с массивами строк
                cursor.execute("CALL insert_many_users(%s, %s, %s)", (names_array, surnames_array, phones_array))

                print("[INFO] Users inserted/updated successfully.")

        elif q == "4":
            limit = int(input("Enter the limit (number of records per page): "))
            offset_page = int(input("Enter the page number (starting from 1): ")) - 1
            offset = offset_page * limit
            get_paginated_data(limit, offset)

        elif q == "5":
            name = input("Enter name to delete (leave empty if deleting by phone): ")
            phone = input("Enter phone to delete (leave empty if deleting by name): ")
            with connection.cursor() as cursor:
                cursor.execute("CALL delete_user_by_name_or_phone(%s, %s);", (name, phone))
                print(f"[INFO] User(s) with name '{name}' or phone '{phone}' deleted.")

        elif q =="6":
            exit()



except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
