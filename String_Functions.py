str="helloo,my name is akuu."

print(str.endswith("uu."))       #to check if substring is the end of the string::gives true

print(str.startswith("hell"))     #to check if substring is start of the string ::returns true

#to capitalize the first element of string but in a new one
print(str.capitalize())          
print(str) #here it is not yet permanent
#to make changes in the string permanently
str=(str.capitalize())     
print(str)

# str.replace("old","new")=>to replace a character or a substring
print(str.replace("Helloo","hii"))               #only replaces it in a new string and is not reassigned to original one

# str.find()=>returns the first index of first occurer of character or a certain word
print(str.find("m"))
print(str.find("name"))
# print(str.find("0"))      #-1 for not present in the string

# str.count("")::counts occurence of substring in string
print(str.count("a"))
print(str.count("is"))


