# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
name=["khushi","sayna","vansh"]
siblings= name.copy()
print(siblings)

siblings=list(name)
print(siblings)

siblings=name[:]  #slice operator
print(siblings)