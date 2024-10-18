# typecasting= the process of convertinga value of one data typeto another(string,float,integer and boolen)

#explicit typecasting 
name="Khushi"
age=18
percentage=92.7
student=True
ag=0

#using type function
print(type(name))
print(type(age))
print(type(percentage))
print(type(student))

age=float(age)
print(age)
print(type(age))

percentage=int(percentage)
print(percentage)
print(type(percentage))

student=str(student)
print(student)
print(type(student))

age=bool(age)
print(age)
print(type(age))

ag=bool(ag)
print(ag)

a=""          #empty string and 0 act as false space ,any other thing than 0 or empty string act as true
a=bool(a)
print(a)

#implicit typecasting
x=2
y=2.0
x=y/x
print(x) 
# it gives float so implicit typecasting is change the variables types automattically by using certain functions