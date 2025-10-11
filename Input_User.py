# we use input() statement

name = input("enter ur name : ")    # type of input() is always string even if it is number or string
print("Welcome", name,"!!")
print(type(name))


# to convert input into int or float ,we then use typecasting::int/float(input())
age=int(input("enter ur age: "))
print(type(age))
marks=float(input("enter ur marks: "))
print(type(marks))