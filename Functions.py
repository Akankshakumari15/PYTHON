# functions::block of statements that perform a specific task
# def func_name(parameter_1,parameter_2):     ::to declare function
# func_name(value_parameter_a,value_parameter_b)     ::to call function

def sum(a,b):
    sum=a+b
    return sum
print("sum: ",sum(2,3))

# greatest of 3 numbers
def greatest(a,b,c):
    if a>b and a>c:
        print("a is greatest")
    elif b>a and b>c:
        print("b is greatest")
    else:
        print("c is greatest")
greatest(1,2,3)


# average of three numbers
def average(x,y,z):
    avg=(x+y+z)/3
    return avg
print(int(average(81,72,94)))     #type casting



# types of functions::two types
# built in functions and "user"-defined functions
# built-in defined:: print, end ,sep, length, type , range
print("Apnacollege",end=" ")   #pass "end" parameter to anything as it is by default /n(next line)
print("akkuuu")


# default paremeters
def calc_prod(a=3,b=3):      #default parameters passed
    print (a*b)
    return a*b

calc_prod(4,7)






