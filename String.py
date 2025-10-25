# string::sequence of characters;valid ways
str1="this is me!"
str2='hii'
str3='''hello'''
str4="This is a string.\tWe are creating it in python"
print(str4)

# escape sequence characters:: tab(\t) nextline(\n)

# concatenation
print(str2+" "+str1)

# length of a string
print(len(str1))     #also counts the empty spaces

# indexing::starts with zero
print(str1[9])
print(str1[0])          #we cannot make changes/assignment in the string using its index


## slicing::accesing parts of  a string
# positive slicing
# str[startingIndex:EndingIndex]    but in this starting is included but not the ending index
name="appleIsHealthy"
print(name[1:4])
print(name[5:len(name)])
# print(name[:4])   #[0:4]
# print(name[1:])   #[1:len(str)]

# negative indexing  :: -5 -4 -3 -2 -1
str="apple"
print(str[-3:-1])   #pl