thisset = {"apple","bnana","cherry"}
print(thisset)

thisset2 = {"apple","bnana","cherry",True, 1,2}
print(thisset2)
print(len(thisset))

print("apple" in thisset)
thisset.add("fareed")
print(thisset)
#remove #discard #pop() # clear #del mathod
sett= {"apple","umer","adeel","haroon","dara"}
for x in sett:
    print(x)
seta={"han g"}
setb = {"kai hua he"}
setc  = seta.union(setb)
print(setc)
seta.update(setb)
print(seta)
#intersection_update
