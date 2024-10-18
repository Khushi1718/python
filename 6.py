#to find prime number betwenn 2 to 100
print("The Prime Numbers Between 2 to 100 are : \n") 
for i in range(2,101,1):
    for j in range(2,i,1):
        if i%j==0:
            break
    else:
        print(i, end=' ')
        

print("The Prime Numbers Between 2 to 100 are : \n")
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        # This else corresponds to the for-loop, not the if-statement
        print(i, end=' ')
