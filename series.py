# n=int(input("entre a number : "))

# a,b=0,1
# for i in range(n):
#     print(a,end=' ')
#     next_number=a+b
#     a=b
#     b=next_number

x=4
for i in range(1,x+1,1):
    # for j in range(1,i+1,1):
        print("*"*i , " "*(x-i))
    # print()

x=4
for i in range(1,x+1,1):
   
        print(" "*(x-i), "*"*i)

n=5
factorial=1
for i in range(1,n+1,1):
        factorial*=i
print(factorial)

# n=int(input())
# for i in range(2,n,1):
#         if n%i==0:
#                 print("not a prime")
#                 break
#         else:
#                 print("prime")
#                 break

Num = int(input("Number: "))  # Use input() in Python 3 instead of raw_input()
sum_value = 0  # Initialize sum to 0

# Loop through numbers from 10 to Num, stepping by 3
for i in range(10, Num, 3):
    sum_value += 1  # Increment the count for each valid number
    if i % 2 == 0:  # Check if i is even
        print(i * 2)  # Print double the value of i
    else:
        print(i * 3)  # Print triple the value of i

print("Sum:", sum_value)  
        
    