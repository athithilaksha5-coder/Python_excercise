#Zero division error
#name error
#value error
#file not found
#Exception Handling --Unexpected event happens at runtime 
# and stops the execution of the program
#unexpected event occurs at runtime and disturbs the 
#normal flow of the program.
#Finally should be in finally
try:
	no1 = int(input("Enter no1:"))
	no2 = int(input("Enter no2:"))
	try:
		
		print(no1/no2) #Exception Occuring area
	
	except ZeroDivisionError: #Python class
		print("Check divisor")
		no2 = int(input("Enter no2:"))
		print(no1/no2)
				  
except ValueError:
	print('give only numbers')
	no1 = int(input("Enter no1:"))
	no2 = int(input("Enter no2:"))
		
except: #Default except block
	print('something went wrong')
finally:  #Executed always # Cleaning Area
	print('finally block')
print("hi")

	



	
	
	
