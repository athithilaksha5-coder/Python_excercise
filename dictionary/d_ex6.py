employee = {}

name = input("What is your name?")

for letter in name:
	employee[letter] = employee.get(letter,0)+1
	
else:
	print(employee)