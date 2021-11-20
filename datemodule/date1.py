import datetime

#get current date and Time
current_datetime = datetime.datetime.now()
print(current_datetime)
#output: 2021-11-18 18:12:30.195187

#Get current date
current_date=datetime.date.today()
print(current_date)
#output: 2021-11-18

#Get datetime attributes using dir() function
print(dir(datetime))
