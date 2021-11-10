l = [10,20,10,20,30,50,60,70,60,10]
count={}

for item in l:
	count[item]=count.get(item,0)+1
else:
	print(count)