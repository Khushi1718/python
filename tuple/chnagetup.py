#Since tuples are unchangeable and unmutable 
# we can make changes in tuple by converting it into list then make changes then covert back into tuple 
name=("khushi","sayna","vansh")
list1=list(name)
list1.append("sushil")
name=tuple(list1)
print(name)

#We can add tuple into other tuple 
tuple1=("khushi")
tuple2=("sayna")
tuple1+= tuple2
print(tuple1)

(x,y,z,k)=name
print(x)
print(y)
print(z)

(x,y,*z)=name
print(z)

(x,*y,z)=name
print(y)
print(z)