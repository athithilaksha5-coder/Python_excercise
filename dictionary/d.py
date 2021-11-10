#create a dictionary

cubes = {1:1,2:8,3:27,4:64,5:125,6:216,7:343,8:512,9:729,10:1000}
print(cubes)

#remove a particular item, returns its value
print(cubes.pop(10))
print(cubes)

#remove an arbitrary item
print(cubes.popitem())
print(cubes)

#remove all items
cubes.clear()
print(cubes)

#delete the dictionary itself
del cubes
#throws error print after delete the dictionary
print(cubes)