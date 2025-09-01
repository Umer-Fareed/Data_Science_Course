class human:
    def __init__(self,a,o):
        self.name = a
        self.occupation = o
    def do_work(self):
        if self.occupation == "tennis":
            print(self.name,"playes tannis")  
        elif self.occupation == "actor":
            print(self.name, "shoot films")
    def speaks(self):
        print(self.name,"say how are you ")
tom = human("tom","actor")
tom.do_work()   
tom.speaks()    
#Program no 2 
 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
p1 = Person("hohn",36)
print(p1.name)
print(p1)
#Qusetino no 3

class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def myfunc(self):
        print("hello my name is ",f"{self.name}  {self.age}")
p1  = Person("john",23)
p1.age = 42
p1.myfunc()
        
        

