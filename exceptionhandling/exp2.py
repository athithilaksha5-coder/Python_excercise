try:
	no1 = int(input())
	no2 = int(input())
	print(no1/no2) #Exception Occuring area
except (ValueError,ZeroDivisionError) as msg: #Handling area
	print(msg)
	print('Give only numbers')
	
except: #Default Except block
	print("Something went wrong")
finally:
	print('finally block')
	
print("hi")
		  
	