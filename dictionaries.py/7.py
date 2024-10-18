#get number of students and number of cources
N=int(input("Entre number of students :"))
M=int(input("Entre number of cources : "))
marks_list=[]
for i in range(1,N+1):
    
    marks=list(map(int,input(f"Entre Marks of M cources for student {i} :").split()))
    marks_list.append(marks)
print(marks_list)

for x in marks_list:
    print(x)

for i in range(N):
    maximum_marks=marks_list[i][0]
    for j in range(M):
        if marks_list[i][j]>maximum_marks:
           maximum_marks=marks_list[i][j]
    print(f"Maximum marks of {i} student is {maximum_marks}")