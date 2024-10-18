myset = {"apple", "banana", "cherry"}
print(myset)
#UNORDERED :Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

#you can add items to sets 
myset.add("orange")
print(myset)

# set1={"khushi","sayna"}
# myset.update(set1)  #in update it must not be the set only 
# print(myset)
list1=["khushi"]
myset.update(list1)
print(myset)

a=set('abc')
b=set('cd')
print(a)
print(b)
print(a^b)

#we can remove items also
myset.remove("khushi")
print(myset)

myset.discard("orange")
print(myset)

myset.pop()
print(myset)

myset.clear()
print(myset)
