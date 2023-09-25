#Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return self.a+self.b
    
    def sub(self):
        return self.a-self.b
    
    def multi(self):
        return self.a*self.b
    
    def div(self):
        return self.a/self.b

a=int(input("Enter the value of A: "))
b=int(input("Enter the value of B: "))
object=Calculator(a,b)
choice=1
while choice!=0:
    print("0. EXIT")
    print("1. ADD")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")

    choice=int(input("Enter your choice: "))
    if choice==1:
        print("Result: ",object.add())
    elif choice==2:
        print("Result: ",object.sub())
    elif choice==3:
        print("Result: ",object.mul())
    elif choice==4:
        print("Result: ",round(object.div(),2))
    elif choice==0:
        print("EXIT")
    else:
        print("INVALID CHOICE!!!")
