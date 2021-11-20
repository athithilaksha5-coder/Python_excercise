import datetime

#datetime.date class
#date object to represent a date(year,month,and day)
d = datetime.date(2015,6,20)
print(d)
#output: 2015-06-20

#Get current date
today = datetime.date.today()
print("Current date=",today)
#output: Current date= 2021-11-18

#Get date from a timestamp
timestamp = datetime.date.fromtimestamp(1326255684)
print("date = ",timestamp)

#Print today year, month, and day
today = datetime.date.today()

print("Current year:",today.year)
print("Current month:",today.month)
print("current day:",today.day)

