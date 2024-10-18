Non_mumbai=[]   #assume a empty list for non mumbai people data 
while True:
    city=input("entre your city name:")
    if city=="quit":
        break
    elif city=="Mumbai":
        continue
    else:
        name=input("entre your name")
        contact=("entre your contact :")
        x=[name,city,contact]
        Non_mumbai.append(x)
print(Non_mumbai)