#Sum all the numbers in a list
def sum(numbers):
	total=0
	for x in numbers:
		total+=x
	return total
	
	
list=[10,20,30,40,80]

print(sum(list))