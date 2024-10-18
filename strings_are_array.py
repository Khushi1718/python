# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
a="hello world"
print(a[4])
print(a[:5])
print(a[0:5])
print(a[2:])
print(a[-1:-12:-1])

for x in a : #since strings are array we can loop through chr in strings

    print(x)
print(len(a))
txt="the best things in life are free !"
if "free" in txt:
    print("Yes, 'free' is present .")
print("expensive" not in txt)
if "expensive" in txt:
    print("true")
else:
    print("false")
