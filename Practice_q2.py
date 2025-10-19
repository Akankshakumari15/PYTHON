# input first anme and find its length
firstName=str(input("Enter ur first name:"))
print("length of ur name is: ",len(firstName))

# to find occurences of "S" in a string
str="sheena loves seashells"
print("No of occurences: ",str.count("s"))

# Greatest of three numbers
a= float(input("input a: "))
b= float(input("input b: "))
c= float(input("input c: "))
if(a>b and a>c):
    print(a," is greatest")
elif(b>a and b>c):
    print(b," is greatest")
else:
    print(c," is greatest")


# to check if multiple of 7 or not
mul = int(input("Enter the number: "))
if(mul%7==0):
    print("it is a multiple of 7.")
else:
    print("it is not a multiple of 7.")
