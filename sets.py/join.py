set1={"a","b","c","d"}
set2={1,2,3,4}
set4={4,5,6,7,8}
set3=set1.union(set2)
print(set3)

set3=set1|set2
print(set3)

set3=set1.union(set2,set4)
print(set3)

set3=set1|set2|set4
print(set3)

set1.update(set2,set4) #it will make changes to orignal set without making new set
print(set1)

set3=set2.intersection(set4)
print(set3)
set3=set2&set4
print(set3)
set2.intersection_update(set4)
print(set2)

set3=set2.difference(set4)
print(set3)
set3=set2 - set4
print(set3)
set2.difference_update(set4)
print(set2)