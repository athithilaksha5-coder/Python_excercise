import re

def isMobileNumber(sentence):
	#pattern = re.compile("(0|91)[6-9][0-9]{9}")
	pattern = re.compile("\d{3}-\d{3}-\d{4}")
	
	return pattern.search(sentence)

sentence = "My mobile no is 082-254-6987"
present = isMobileNumber(sentence)

if (present):
	print("Mobile number is present in the sentence")
else:
	print("Mobile number is not present in the sentence")
	
		
#Mobile number is present in the sentence
#332-542-9647