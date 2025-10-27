# lists methods

list=["akuu", 97.8 , "jabalpur", 19 , "sleeping"]
print("Original list: ",list)

# to add one element at the end
list.append("hiii")
print("Appended list: ",list)

# to sort list in ascending order
num=[3,1,7,5]
num.sort()
print("Sorted list(Ascending): ",num)

# to sort list in descending order::reverse the sort method
num.sort(reverse=True)
print("Sorted list(Descending): ",num)

# to reverse ur lists
num.reverse()
print("Reversed list: ",num)
list.reverse()
print("Reversed list: ",list)


# to insert element at any index
list.insert(0,"helloo")
print("Inserted list: ",list)

# to remove first occurence of a element
inp=[0,5,67,7,4,67,0,0,43,2,8]
inp.remove(2)
inp.remove(0)
print(inp)

# to remove element at any particular index
inp.pop(4)
print(inp)