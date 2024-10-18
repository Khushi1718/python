name=input("entre your name:")
age=input("entre your age :")
age=int(age)
print(f"{name} age is: {age}")

item=input("entre the item you want to buy ")
price=int(input("entre the price "))
quantity =int(input("entre the quantity "))
total = price*quantity
print(f"I want to buy {item} which costs {price} for unit {quantity} and my total bill is {total}")