# dictionaries
# important data structures of python

# dictionaries are used to store data values in "key:value" pairs
# these are mutable(changeable) , unordered and dosen't allow duplicate keys

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
print(info)
print(type(info))   #class::dict(dictionary)

# # properties of dictionary
# unordered::i.e no index
# mutable::i.e changeable
# no duplicate keys allowed

# to access a certain key of a dictionary
print(info["name"])
print(info["topics"])

# to change any value of keys in the dictionary
info["name"]="akanksha"
print(info)

# to add a new key:value pair
info["surname"]="kumari"
print(info)

# if u try to create two keys with same name then the second will be legal and the first key gets overrided.

# an empty dictionary can also be created
null_dict={

}
print(null_dict)
null_dict["college"]="BGIEM"
print(null_dict)


# nested dictionaries
student={
   "name":"akuu",
   "subjects":{
       "maths":"97.4",
       "science":"65.8",
       "english":{
           "literature":"100",
           "grammar":"89.9"
       }
   }
}
print(student)  #to print the whole dictionary
print(student["subjects"])   #to print the sun dictionary
print(student["subjects"]["english"])   #to print the sub-sub dictionary
print(student["subjects"]["english"]["literature"])   #to print a certain key's value only