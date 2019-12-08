def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("enter your choice: 1.addition \n 2.subtraction \n 3.multiplication\n 4. division")
choice=str(input("enter choice:"))
num1=input("enter num1")
num2=input("enter num2")

if choice=='1':
    print("addition of " +num1+ " and "+num2+" is ",addition(num1,num2) )
elif choice=='2':
    print("subtraction of "+num1+ " and "+num2+" is ",subtraction(num1,num2))
elif choice=='3':
    print("multiplication of " +num1+ " and "+num2+" is ",addition(num1,num2) )
elif choice=='4':
    print("division of "+num1+ " and "+num2+" is ",subtraction(num1,num2))
else:
    print("invalid number")