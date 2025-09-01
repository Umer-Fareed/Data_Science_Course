#LOOP LIST
thislist = ["apple","bnana","charry"]
for x in thislist:
    print(x)
for i in range(len(thislist)):
    print(thislist[i])
#LIST COMPRIHENSION
fruits=["apple","bnana","charry","kiwi","mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

newlist2 = [x for x in fruits if x != "apple"]
thislist=[]
print(thislist)
list2=["orange","Mango","kiwi","Pineapple","bnana"]
list3=[100,23,40,53,66]
list3.sort(reverse=True)
list2.sort()
print(list2)
print(list3)

#Coping a List
thislist=[2,4,5,3,2,3,4]
list2=thislist.copy()
print(list2)
print(thislist)
list3=list(list2)
print(list3)
#Join 2 lists
list1=[12,42,53,23,53,4]
list2=["s","g","a"]
list3=list1 + list2
print(list3)
#append
for x in list2:
    list1.append(x)
print(list1)
#extend
list1.extend(list2)
print(list1)

exp = [2200,2350,2600,2130,2190]
print("in fab i spend ",exp[1]-exp[0])
print(exp[0]+exp[1]+exp[2])
if 2000 in exp:
    print("yes i spend 2000 in a month")
else:
    print("no i not spend such money")
exp.append(1842)
print("expenses at the end of june",exp)
exp[3]= exp[3]-200
print(exp)
