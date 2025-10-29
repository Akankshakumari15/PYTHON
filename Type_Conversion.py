# type conversion(automatically) and type casting(manually)


# type conversion
a=1           #python aotumatically converts int  into  float
b=2.7
# c="3"  =>error in adding string to int
sum=a+b          #1.0+2.7=>3.7
print(sum)

# type casting
c=int("2")
e=float("6")
d=5.6
print(type(c))
print(c+d)

p=str(3.14)
print(type(p))    #conversion to string