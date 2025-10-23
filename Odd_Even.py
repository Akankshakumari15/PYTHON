# if elif else loop
number= int(input("Enter ur number: "))
if number%2==0:
    print(number,"is even.")
else:
    print(number,"is odd.")



# while loop::odd numbers
i=1
while i<=10:
    if i%2==0:
        i+=1
        continue #skip
    print(i)
    i+=1


# for loop::even numbers
for i in range(2,101,2):
    print(i)


#  for loop::odd numbers
for j in range(1,102,2):
    print(j)