import datetime

t1 = datetime.date(year = 2018,month = 4, day = 4)
t2 = datetime.date(year = 1996,month = 2,day = 26)
t3,t4,t5 = t1.year-t2.year,((t1.year-t2.year)*12+(t1.month-t2.month)),t1-t2
print(t1)
print(t2)
print("calculate number of year,month and days between two dates")
print("No.of.Year:",t3,"No.of.Month:",t4,"No.of.Days:",t5)

