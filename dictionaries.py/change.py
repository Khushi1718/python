thisdict = { "brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"]=2018
print(thisdict)
thisdict.update({"year":2020})
print(thisdict)
thisdict.update({"color":"white"})
print(thisdict)
thisdict.pop("color")
print(thisdict)
del thisdict["brand"]
print(thisdict)