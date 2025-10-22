# store following meanings in apython dictionary
dict={
      "cat":"a small animal",
    "table":["a piece of furniture","lists of facts and figures"]
  
}

print(dict)


# list of subjects for students.one classrom is required for 1 subject. how many classrooms are needed by all students.
set={"python","java","C++","python","javascript","java","python","java","C++","C"}
print(set)

# to calculate no of classrooms needed::we can just find the length of set that counts only unique items
print("No. of classrooms needed: ",len(set))


# enter marks of three subjects from user and store in dict.start with empty.use sub name as key and marks as value
dict={}
# dict.update({"chemistry":int(input("Enter marks of chemistry: "))})
# dict.update({"physics":int(input("Enter marks of physics: "))})
# dict.update({"maths":int(input("Enter marks of maths: "))})
# print(dict)


# figure out a way to store 9 and 9.0 as separate values in the set
# 1st solution::string
num={"9","9.0","8","8.0"}
print(num)
# 2nd solution::stor ein form of tuples
num1={("float",9.0),("int",9)}
print(num1)