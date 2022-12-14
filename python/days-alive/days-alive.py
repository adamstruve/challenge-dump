from datetime import date, datetime
date_format = "%m/%d/%Y"
today =  date.today()
today = today.strftime(date_format)
your_birthday = input("Your birthday (Example: 07/11/1997): ")
a = datetime.strptime(your_birthday, date_format)
b = datetime.strptime(today, date_format)
delta = b - a
print(f"As of today you are {delta.days} days old.")


