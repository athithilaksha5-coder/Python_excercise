def findEvenNumbers(l):
	if l%2==0:
		return True
	else:
		return False
	
l = [1,3,5,6,47,52,34]
l2=list(filter(findEvenNumbers,l))
print(l2)