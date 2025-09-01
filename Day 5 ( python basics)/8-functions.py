def my_func(a ,b):
    print(a + " fareed " + b)
my_func("umer","fareed")
def data(*kids):
    print("the youngest child is " + kids[2])

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_func(fname):
  print(fname + "refsnes")

my_func("email")
my_func("tobias")
my_func("linus")

#Arbitrary Arguments
def my_function(*book):
  print("there are some " + book[0])
my_function("email","tobalis","limus")

#keyword arguments
def thisfunc(lahore,karachi,islambad):
  print("this is a city of " + lahore)

thisfunc(lahore="big",karachi="derty",islambad="beauty")

#Arbitrary Keyword arguments
def func2(**girl1):
  print("there are two" + girl1["girl3"])
func2(girl1="laiba",girl2="isha",girl3="zoha")

#Default Parameter Value
def country( cnt = "norway"):
  print("i am from " + cnt )
country("pakistan")
country()
country("india")

#Passing list as a argument
def func3(fruits):
  print(fruits)

fruits=["mango","bnana","apple","charry"]
func3(fruits)

#return velue
def multi(a):
  return (5 * a)
print(multi(4))
print(multi(5))

#positional arguments
def func4(x, /):
  print(x)
func4(3)

def my_function(x):
  print(x)

my_function(x = 3)

#keyword only arguments
def func5(* , x):
  print(x)
func5(x = 6)

#combine keyword and positinal arguments
def func6(a,b,/,*,c, d):
  print(a + b + c + d)
func6(5,4,c = 44, d = 535)

#recursion function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

