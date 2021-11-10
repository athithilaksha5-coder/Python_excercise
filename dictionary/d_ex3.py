# Count of each letter in a given word using dictionary
employee={}
name = input("What is your name?")

#for letter in name:
	#employee[letter] = employee.get(letter,0)+1
#else:
	#print(employee)
	
	
for i in name:
	if i not in employee.keys():
		employee[i] =1
	elif i in employee.keys():
		employee[i]+=1
print(employee)
	
	
	
