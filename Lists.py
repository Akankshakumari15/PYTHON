# lists and tuples::arrays 
# at once u can also store different types of details without any condition

marks=[97,87.5,65,97.9,100]

print(marks)
print(type(marks))  #lists

print(marks[3])  #to access a certain index of the lists

print(len(marks))  #to find length of string

list=["akanksha", 19, "jabalpur", 87.4]  #valid string

# difference between string and lists in python 
# strings are immutable(cannot be changed)::can access indexes but not change them
# lists are mutable(can be changed)::can access indexes and change them too

str="hello"
# str[0]=j      #python does not support this
list[0]="akuu"  #mutable list::i.e can be changed
print(list)

# a non existent index in a lists cannot be accessed and will always give a out of range error
# print(list[6])


