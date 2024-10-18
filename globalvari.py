x="awesome"       #global variable
def myfunc():
    x="fantastic"          #local variable
    print("python is" + x)
myfunc()
print("python is"+ x)  

#to make the global variable inside the function by using keyword global
def myf():
    global x    
    x= "fantastic"
myf()
print("python is ", x)

x= "awesome"
def myff():
    global x
    x="fantastic"
myff()
print("python  is ", x)