# sort the list by allphabetical order
list=["orrange","apple","mango","kiwi","banana"]
list.sort()
print(list)
# sort the list alphabetically
list1=[100,50,20,10,40,2]
list1.sort()
print(list1)
#sort the list descending
list.sort(reverse= True)
print(list)
list1.sort(reverse = True)
print(list1)
#customize sort function
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)
# to make case insensitive sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist)
#built in function to make case in senstive sort function 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse method
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
