from datetime import datetime, timedelta

current_date = datetime.now()

for i in range(1,6,1):
    date = current_date + timedelta(days=i)
    print(date.strftime("%d.%m.%Y %A"))
