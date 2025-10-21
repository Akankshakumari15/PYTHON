# loops::while and for

# while loop
str="hello"
count=0         #iterators
while count<5:
    print("hello",count)
    count+=1    #iteration


# print numbers from 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

# print numbers from 5 to 1
i=5
while i>=1:
    print(i)
    i-=1



# important keywords::break and continue


# break::used to terminate loop
i=1
while i<=5:
    print(i)
    if i==3:
        break            #loops ends at i=3 or that is it breaks
    i+=1


# continue::terminates execution in current situation in current iteration 
j=0
while j<=5:
    if j==3:
        j+=1
        continue   #only 3 is omitted or terminated in the whole cycle
    print(j)
    j+=1



# for loop
list=[2,3,5,7]
for i in list:      
    print(i)


str="Akanksha"
for char in str:
    print(char)


# an optional "else" with for loop
string="apnacollege"
for char in string:
    if(char=='o'):
        print("o found")
        break
    print(char)
else:
    print("end")    



# range() function in for loop
# returns sequence of numbers , starts from 0 by default and increments+1 by default
# syntax:: range(start,!stop!,step)
# skips the last element(not included)
for i in range(5):
    print(i)     # 0 1 2 3 4
for i in range(2,10):
    print(i)    # 2 3 4 5 6 7 8 9 
for i in range(4,8,2):
    print(i)    # 4 6



# pass() statement::to skip any work in the loop::to write a null statement
for i in range(10):
    pass