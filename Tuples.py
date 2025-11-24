# Tuples::similar to lists
# lets us create immutable sequences::"no external changes allowed"
# while lists uses [] tuples use()

tup=(76.6,4,5,3,3,532,2,2,0,40,45)
print(tup)
print(type(tup))    # class = tuple

# to print values of tuples
print(tup[2])

tuple=()    #empty tuple but valid
print(tuple)
print(type(tuple))


# to create a single value tuple ::add a comma to the single element "mandatorily" otherwise the tuple type will get regarded as int or float
tuples=(1,)
print(tuples)

# tuple slicing:: ending index is not included in the sliced substring
print(tup[2:5])
print(tup[:3])
print(tup[0:])


