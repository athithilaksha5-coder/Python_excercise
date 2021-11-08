def bubblesort(array):
	

	for i in range(len(l)-1,-1,-1):
		for j in range(0,i):
			if l[j]>l[j+1]:
				l[j],l[j+1]=l[j+1],l[j]
		

l=[10,9,8,7,6,5,22,1]

bubblesort(l)

print("sorted array in ascending order:",l)
