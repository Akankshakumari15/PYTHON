# if-elif-else loop
age = int(input("Enter ur age: "))

if age >= 18 and age <= 70:
    print("Eligible to vote.")
elif age > 70:            
    print("Not eligible to vote.")    #indentation::proper spacing
else:
    print("Too small!!")


# example
Grade=int(input("Students marks: "))
if Grade>=90:
    print("A")
elif Grade>90 and Grade<=80:
    print("B")
elif Grade>80 and Grade<=70:
     print("C")
else:
    print("D")




# nesting of loops
if age>=18:
    if age<=70:
        print("Can drive.")
    else:
        print("CANNOT drive.")