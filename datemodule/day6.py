from datetime import datetime,date,timedelta

t1 = date(year = 2018, month=7,day = 12)
t2 = date(year = 2017,month = 12, day = 23)
t3 = t1 - t2
print("no of days:",t3)

t4 = datetime(year=2018, month = 5, day = 15, hour=8,minute = 25,second = 45)
t5 = datetime(year=2017, month = 7, day=14, hour = 5 , minute = 20, second = 58)
t6 = t4 - t5
print("date and time:",t6)

print(type(t3))
print(type(t6))

#difference between two timedelta objects
t7 = timedelta(weeks = 2,days = 5)
t8 = timedelta(days = 4,hours = 10)
t9 =t7-t8
print("timedelta:",t9)

#Time duration in seconds
t = timedelta(days = 5,hours = 1, seconds = 33, microseconds = 32547)
print("Total seconds:",t.total_seconds())


