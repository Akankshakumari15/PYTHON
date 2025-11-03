
# # Greatest of three numbers
# a= int(input("input a: "))
# b= float(input("input b: "))
# c= float(input("input c: "))
# if(a>b and a>c):
#     print("{} is greatest".format(a))
# elif(b>a and b>c):
#     print(b," is greatest")
# else:
#     print(c," is greatest")



# sum = 0
# count = 0
# a = input("a: ")   

# for dig in a:
#     if int(dig) % 2 == 0:
#         sum += int(dig)
#         count += 1

# print("sum:", sum, "count:", count)


# num=4
# fact=1
# for i in range(2,num+1):
#     fact=fact*i

# print(fact)

# a = int(input("input a: "))
# b = int(input("input b: "))

# for num in range(a, b + 1):
#     if num > 1:  # prime numbers are greater than 1
#         for j in range(2, num):
#             if num % j == 0:
#                 break
#         else:
#             print(num)


# s = input("Enter a string: ")
# # s[start:end:step]  so if step is -1 it directly reverses the string
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")



# n = int(input("Enter a number: "))
# temp = n
# rev = 0

# while n > 0:
#     dig = n % 10
#     rev = rev * 10 + dig
#     n //= 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# armstrong no
num = int(input("Enter a number: "))
original_num = num
num_str = str(num)
digits = len(num_str)
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

if sum == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
