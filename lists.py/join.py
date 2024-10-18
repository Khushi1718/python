name=["khushi","sayna","vansh","khushi"]
name1=["geeta","sushil","bimla"]
list= name+name1
print(list)


for x in name1:
    name.append(x)
print(name)

name.extend(name1)
print(name)

print(name.count("khushi"))
print(name.count("sayna"))
print(name.index("khushi"))
print(name.index("sayna"))
