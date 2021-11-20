import re

def isMobileNumber(sentence):
	pattern = re.compile("(0|91)[6-9][0-9]{9}")
	return pattern.search(sentence)

sentence="My mobile no is 919635478966"
print(isMobileNumber(sentence))