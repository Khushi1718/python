# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
dict1={"brand":"jaat","model":"super"}
print(dict1)
x=dict1["brand"]
print(x)
x=dict1.get("brand")
print(x)
x= dict1.keys()
print(x)

dict1["color"]="white"
x= dict1.keys()
print(x)
x=dict1.values()
print(x)
x=dict1.items()
print(x)