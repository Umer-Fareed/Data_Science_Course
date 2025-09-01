'''thisdict = {
    "brand":"frari",
    "modal":"mastang",
    "year": 1982,
}
print(thisdict)
x = thisdict["brand"]
print(x)
x =thisdict.get("brand")
print(x)
x = thisdict.keys()
print(x)
thisdict["color"] = "black"
print(thisdict)
y = thisdict.items()
print(y)'''
bike = {
    "color":"red",
    "modal":"cd",
    "year": 2013,
}
print(bike)
bike.update({"brand":"honda"})
print(bike)
bike.pop("brand")
print(bike)
bike.popitem()
print(bike)
del bike ["color"]
print(bike)
bike.clear()
print(bike)
bike2 = {
    "color":"red",
    "modal":"cd",
    "year": 2013,
}
for x in bike2:
    print(bike2[x])
for x in bike2.keys():
    print(x)
#Nested dictionary

