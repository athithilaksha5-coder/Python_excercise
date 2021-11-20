from datetime import datetime, date

t1 = datetime(year = 1996,month = 2,day= 26)
t2 = datetime(year = 2018,month = 4,day = 4)
d1,d2,d3= t2.year-t1.year,((t2.year-t1.year)*12+(t2.month-t1.month)),t2-t1

print(d1,d2,d3)