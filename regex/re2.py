import re

def isLandLine(sentence):
	pattern = re.compile(r'((91|0)\d{2,4})-([1-9][0-9]{5,7})')
	s = pattern.search(sentence)
	std = len(s.group(1))
	print(std)
	
	phone = len(s.group(3))
	print(phone)
	if (std+phone)==12:
		return True
	elif (std+phone)==11:
		return True
	else:
		return False
	
sentence = "My number is 044-365478"

print(isLandLine(sentence))
