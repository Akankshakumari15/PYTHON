# input 3 movies and store in a list 
movie1 = input("Input ur favourite movie: ")
movie2 = input("Input ur favourite movie: ")
movie3 = input("Input ur favourite movie: ")

list=[]
list.insert(0,movie1)
list.insert(1,movie2)
list.insert(2,movie3)
print(list)

# second way
movie=[]
movie.append(input("Input ur favourite movie: "))
movie.append(input("Input ur favourite movie: "))
movie.append(input("Input ur favourite movie: "))
print(movie)



# check if a list contains a palindrome of elements
pal = [1, "akuu", "akuu" ,1]
print("Original list: ",pal)

pal1=pal.copy()
print("Copied list: ",pal1)

pal1.reverse()
print("Reversed list: ",pal1)

if pal==pal1:
    print("It is a palindrome.")
else:
    print("It is not a palindrome. ")


# count no of students with "a" grade
tup = ("c", "d", "a", "a", "b", "b", "a")
print("No of occurrences of 'a':", tup.count("a"))



# store above values in a list and sort them from "a" to "d"
list=["c", "d" , "a", "a", "b", "b", "a"]
list.sort()
print("Sorted list: ",list)
