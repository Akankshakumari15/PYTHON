# while loop

# print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1


# print numbers from 100 to 1
j=100
while j>=1:
    print(j)
    j-=1



# print multiplication table of n
n=int(input("enter a number: "))
i=1
while i<=10:
     mul=n*i
     print(n,"*",i,"=",mul)
     i+=1


# print elemnts of following list using loop
# (1,4,9,16,25,36,49,64,81,100)
list=[1,4,9,16,25,36,49,64,81,100]
i=0
count=0
while len(list)>count:
    print(list[i])
    count+=1
    i+=1


# search for  a number x in the tuple using loop
# (1,4,9,16,25,36,49,64,81,100)
tuple=(1,4,9,16,25,36,49,64,81,100)
i=0
m=int(input("enter a number u want to search: "))
while i< len(tuple):
    if(m==tuple[i]):
          print(m,"found at index",i)
    i+=1

         

# print elements of following list usinf a for loop
# [1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
for i in nums:
     print(i)

# search a number x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100,4)
x=int(input("enter a number: "))
index=0
for i in tup:
     if(i==x):
          index+=1
          print(i,"found at index",index)
          break


# print 1 to 100 using range()
for i in range(1,101,1):
     print(i)


# print numbers from 100 to 1
for i in range(100,0,-1):
     print(i)


# print multiplication table of a no
n=int(input("enter no:"))
for i  in range(1,11):
     print(n*i)



# find sum of first n numbers::using for
x=int(input("enter no:")) 
sum=0
for i in range(1,x+1):
     sum=sum+i
print(sum)
# using while 
i=0
m=int(input("enter no:")) 
sum2=0
while i!=m+1:
     sum2=sum2+i
     i+=1
print(sum2)



# find factorial of a number n using for loop
f=int(input("enter no for factorial:")) 
fact=1
for i in range(1,f+1):
     fact=fact*i
print("factorial: ",fact)