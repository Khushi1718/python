name=["khushi","sayna","vansh","sushil","bimla"]
fruit=["mango","orange"]
name[0]="geeta"
name[1:2]="nana","sayna"
print(name)
name[1:3]="khushi","geeta"
print(name)
name.insert(4,"robin")
print(name)
name.append("kkhushi") #add the given element in last
print(name)
name.extend(fruit)  #add elements of list fruits to name list
print(name)
name.remove("sushil")
print(name)
name.pop()   #remove last 
print(name)
name.pop(1)  #remove the specified index element
print(name)
del name[0]
print(name)
name.clear()
print(name)