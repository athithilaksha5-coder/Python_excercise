from datetime import time

#time object to represent time
a = time()
print("a =",a)

#time(hour,minute,second)
b = time(15,45,58)
print("b =",b)

#time with variable name
c = time(hour = 15,minute = 45, second=58)
print("c = ",c)

#hour, munute, second,microsecond
d = time(15,45,58,58974)
print("d = ",d)
