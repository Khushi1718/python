#assume a empty matrix 
matrix=[]
for i in range(2):
    row=[]
    for j in range(2):
        value=int(input(f"entre value for [{i+1},{j+1}] :"))
        row.append(value)
    matrix.append(row)
for row in matrix:
    print(row)

list1=[1,2,3]
list1.append(4)
print(list1)

