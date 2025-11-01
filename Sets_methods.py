# sets methods

collection={2,4,5,6,3,"byee","hiiii"}
nums={3,4,5,"hello","akuu","byee",3}

# we can add and remove items from a sets but not change the existing items in the set

# to add an element
collection.add("helloo")
collection.add(8)
collection.add((13,42))   #tuple
print(collection)

# to remove an element
collection.remove(8)
print(collection)

# to remove a random variable
print(collection.pop())

# combines both set values and returns new set
print(collection.union(nums))

# combines common values and returns new set
print(collection.intersection(nums))

# empty the set
collection.clear()
print(collection)