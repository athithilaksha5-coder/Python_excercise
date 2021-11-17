#addition
result = lambda no1,no2: no1+no2
print(result(10,20))

#find greatest number

result = lambda no1,no2: no1 if no1>no2 else no2
print(result(25,14))

#Variable length argument with lambda

result = lambda *no: no
print(result(5,3,5))