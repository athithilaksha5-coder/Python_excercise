def string_test(string):
	d={'uppercase':0,'lowercase':0,'digits':0,'specialcharacter':0}
	for x in string:
		if x.isupper():
			d['uppercase']+=1
		elif x.islower():
			d['lowercase']+=1
		elif x.isdigit():
			d['digits']+=1
		else:
			d['specialcharacter']+=1
	return d
	
result = string_test("HeLLoPython!34")

for k,v in result.items():
	print(k,"--->",v)
	
		