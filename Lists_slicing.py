# lists slicing

list=["akuu", 97.8, "jabalpur", 19]
print(list)

# to slice :: list_name[start_index:end_index]
## ending index is not included in the sliced substring
print(list[0:2])

print(list[0:])  #same as list[0:len(list)]

print(list[:3])  #same as list[0:4]

# negative slicing::-4,-3,-2,-1
print(list[-3:-1])   #[97.8,jabalpur]