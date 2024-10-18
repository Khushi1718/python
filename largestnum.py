#to find the maximum number'
list1=[1,10,22,33,45,37,77]
max=list1[0]  #assume the maximum value is list1[0]
for x in list1:
    if x>list1[0]:
        max=x
print("The maximum value is:" , max)