#Method1
# making a calculator to work on two Parameter(numbers) using class
class Calculator:
    def __init__(self, n1,n2):
        self.n1= n1
        self.n2= n2

    def adding (self):
        return self.n1+self.n2
    def multiply(self):
        return self.n1*self.n2
    def subtract(self):
        return self.n1-self.n2
    def Divide(self):
        return self.n1/self.n2


print(" Choice 1 : Add \n", "Choice 2 : Subtract \n", "Choice 3 : Multiply \n", "Choice 4 : Divide \n" )

N = 0
while N==0:
    choice = float(input("Enter choice:"))
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    if choice == 1:
        A = Calculator(n1, n2)
        print(A.adding())
    elif choice == 2:
        B = Calculator(n1, n2)
        print(B.subtract())
    elif choice == 3:
        C = Calculator(n1, n2)
        print(C.multiply())
    elif choice == 4:
        D = Calculator(n1, n2)
        print(D.Divide())
    else:
        N==1
        print("Enter valid choice!")