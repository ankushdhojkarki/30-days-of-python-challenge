#1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
print(f"Day: {now.day}, Month: {now.month}, Year: {now.year}, Hour: {now.hour}, Minute: {now.minute}, Timestamp: {now.timestamp()}")

#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time)

#3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_obj = datetime.strptime(date_string, "%d %B, %Y")
print(date_obj)

#4. Calculate the time difference between now and new year.
from datetime import date, datetime

today = date(year=2026, month=1, day=16)
new_year = date(year=2027, month=1, day=1)
time_until_new_year = new_year - today
print(time_until_new_year)

#5. Calculate the time difference between 1 January 1970 and now.
today = date(year=2026, month=1, day=16)
given_date = date(year=1970, month=1, day=1)
time_until_new_year = today - given_date 
print(time_until_new_year)



