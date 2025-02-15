from datetime import datetime

date1_str = input("Enter the first date (dd.mm.yyyy HH:MM:SS): ")
date2_str = input("Enter the second date (dd.mm.yyyy HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%d.%m.%Y %H:%M:%S")
date2 = datetime.strptime(date2_str, "%d.%m.%Y %H:%M:%S")

difference_in_seconds = abs((date2 - date1).total_seconds())

print(f"Difference in seconds: {difference_in_seconds}")
