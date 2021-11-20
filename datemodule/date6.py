from datetime import datetime

#current date and time
now = datetime.now()
print("current_time:",now)

t1 = now.strftime("%H:%M:%S")
print(t1)

t2 = now.strftime("%y/%m/%d, %H:%M:%S")
print(t2)

#Minutes(%M) Locale's AM or PM(%p)
d = now.strftime("%I:%M %p")
print(d)

#%B

d1 = now.strftime("%B")
d2 = now.strftime("%b")
print(d1,d2)

#%A -- full weekday name %a -- abbreviated weekday name

d3 = now.strftime("%d %b %y %A %a %w")
print(d3)












