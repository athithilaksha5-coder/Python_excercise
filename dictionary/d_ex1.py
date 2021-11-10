result = {}

count = int(input("Enter no.of students :"))

while count>0:
	name = input("Enter student name:")
	per = input("Enter student percentage:")
	result[name] = per
	count -=1
	
#else:
	#print(result)
	
for i in result:
	print(i, "=====>",result[i])
	
	
print(result.keys())
print(result.values())
print(result.items())
	
	