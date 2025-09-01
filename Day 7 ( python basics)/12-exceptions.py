x= input("enter number1: ")
y= input("enter number2: ")
try:
    z = x/ int(y)
except ZeroDivisionError as e:
    print('Divisino by zero exception')
    z = None


except Exception as e:
   print('exception type:',type(e).__name__)
   z = None
print('devision is : ', z)
