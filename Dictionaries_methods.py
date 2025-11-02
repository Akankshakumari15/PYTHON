# dictionaries methods

info={
    "key":"value",
    "name":"akuuu",
    "cgpa":8.2,
    "age":19,
    "city":"jabalpur",
    "subjects":["python","c++","dsa"],
    "topics":("dict","sets"),
    "is_adult":True
}

# to get all keys of the dictionary
print(info.keys())

# typecasting::to convert dictionary into list or tuple
print(list(info.keys()))
print(tuple(info.keys()))

# to find total no. of keys in the dictionary
print(len(info))   #print(len(list(info.keys())))

# returns all values
print(info.values())
print(list(info.values()))

# reurns all (key,value) pairs as tuples
print(info.items())
pairs=list(info.items())
# to get a certain pair of key value
print(pairs[4])

# returns all keys according to values
print(info.get("name"))

# to insert specified items to the dictionary
new_dict={
   "gesture":"hii"
}
info.update(new_dict)  #info.update({"gesture":"hii"},{"age":"20"})
print(info)