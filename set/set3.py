#Differnece between discard() and remove()

my_set = {1,5,8,9,10,7,24}
print(my_set)

#discard an element
my_set.discard(8)
print(my_set)

#remove an element
my_set.remove(1)
print(my_set)

#discard an element not present in my_set
my_set.discard(2)
print(my_set)

#remove an element not present in my_set
#my_set.remove(2)
#print(my_set)

#remove an element using pop() method
#remove random element
my_set.pop()
print(my_set)

#clear my_set
my_set.clear()
print(my_set)
