class Calci:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def addition(self):
        return self.x+self.y
    def subtraction(self):
        return self.x-self.y
    def multiplication(self):
        return self.x*self.y
    def division(self):
        return self.x/self.y


def main():
    print("enter your choice:\n 1.addition \n 2.subtraction \n 3.multiplication\n 4. division")
    choice=int(input("enter choice:"))

    if choice==1:
        print "addition: ",calci.addition()
    elif choice==2:
            print "subtraction: ",calci.subtraction()
    elif choice==3:
        print "multiplication: ",calci.multiplication()
    elif choice==4:
        print "division: ",calci.division()
    else:
        print "invalid number"
    print "do you want to continue(y/n): "
    option = str(input("enter y if you want to continue "))
    if option == 'y':
        main()
    else:
        print "thank you! welcome soon...."

fn=float(input("enter first number: "))
sn=float(input("enter second number: "))
calci = Calci(fn,sn)
main()

