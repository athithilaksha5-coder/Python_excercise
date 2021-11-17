def findOddNumber(l):
	if l%2!=0:
		return True
	else:
		return False
		
l = [1,2,3,5,67,7,5,74,52,48,21]
l2=list(filter(findOddNumber,l))
print(l2)