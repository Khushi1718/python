name=["khushi","sayna","vansh","geeta","sushil","bimla"]
for x in name:
    print(x , end=' ')

for i in range(len(name)):
    print(name[i])

x=0
while x<len(name):
    print(name[x] , end=' ')
    x+=1

[ print(x) for x in name ]