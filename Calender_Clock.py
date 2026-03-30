import calendar
import time  

#  for the calender
year=int(input("Enter the Year ")) #year
month_name= input("Enter month name ")   #month
from datetime import datetime
month_number= datetime.strptime(month_name.capitalize(), "%B").month
print(calendar.month(year, month_number)) #display the year calendarnumber

# for the current time
timestamp=time.strftime("%H:%M:%S")
print("Current time is-", timestamp)