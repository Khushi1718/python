Data=[]

while True:
    age=int(input("entre your age :"))  #getting age of individuals
    if age<0:
       break
    elif age>=18:
       continue
    else:
        name=input("entre your name:")
        contact=input("entre your contact number:")
        x=[age,name,contact]
        Data.append(x)
print(Data)