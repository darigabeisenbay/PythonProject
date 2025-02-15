from datetime import datetime, timedelta

date_str = input("Enter a date (dd.mm.yyyy): ")
input_date = datetime.strptime(date_str, "%d.%m.%Y")

yesterday = input_date - timedelta(days=1)
today = input_date
tomorrow = input_date + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%d.%m.%Y %A"))
print("Today:   ", today.strftime("%d.%m.%Y %A"))
print("Tomorrow:", tomorrow.strftime("%d.%m.%Y %A"))
