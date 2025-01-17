# 1) 

class Demo:
    var1 = "Value"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def Fun(self):
        print(f"Fun Method: Parameter 1  = {self.x}, Parameter 2 = {self.y}")

    def Gun(self):
        print(f"Gun Method: Parameter 1 = {self.x}, Parameter 2 = {self.y}")


Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)


Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()



# 2) 

class Bookstore:
    NoofBooks=0
    def __init__(self,name,author):
        self.name = name
        self.author = author
        Bookstore.NoofBooks += 1
    def Display(self):
        print(f"{self.name}. No of books : {Bookstore.NoofBooks}")

Obj1=Bookstore("Linux System Programming","Robert Love")
Obj1.Display()

Obj2=Bookstore("C Programming","Robert Love")
Obj2.Display() 
        


# 3)


class Circle:
    PI = 3.14
    def __init__(self):
        self.radius=0
        self.area = 0
        self.circumference = 0
    def Accept(self,radius):
        self.radius = radius
        
    def CalculateArea(self):
        self.area = Circle.PI * radius ** 2
        
    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * radius
        
    def Display(self): 
        print(f"radius is {self.radius} Area is {self.area} Circumference is {self.circumference}")
        
    
radius = float(input("enter the radius"))
obj1 = Circle()
obj1.Accept(radius)
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()
    


#4 )

class BankAccount:
    ROI=10.5
    
    def __init__(self,name,amount):
        self.name = name 
        self.amount = amount
    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.amount += deposit_amount
        
    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI) / 100
        print(f"the interest is {interest}")
        
        
    def Withdraw(self):
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        self.amount -= withdraw_amount
        
    def Display(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.amount:.2f}")
account1 = BankAccount("Lohith", 15000.00)
account1.Display()
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()
account1.Display()

account2 = BankAccount("Kumar", 10000.00)
account2.Display()
account2.Deposit()
account2.Withdraw()
account2.CalculateInterest()
account2.Display()

 

#5 )

class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        factors = [i for i in range(1, self.Value) if self.Value % i == 0]
        return factors

    def SumFactors(self):
        return sum(self.Factors())

num1 = Numbers(28)
print(num1.ChkPrime())
print(num1.ChkPerfect())
print(num1.Factors())
print(num1.SumFactors())


num2 = Numbers(28)
print(num2.ChkPrime())
print(num2.ChkPerfect())
print(num2.Factors())
print(num2.SumFactors())



# 6 )

class Numbers:
    def __init__(self):
        self.x = 0
        self.y = 0

    def Accept(self):
        self.x = float(input("Enter the first value (x): "))
        self.y = float(input("Enter the second value (y): "))

    def Addition(self):
        return self.x + self.y

    def Subtraction(self):
        return self.x - self.y

    def Multiplication(self):
        return self.x * self.y

    def Division(self):
        if self.y == 0:
            return "Division by zero is not allowed"
        return self.x / self.y



obj1 = Numbers()
obj1.Accept()
print(f"Addition: {obj1.Addition()}")
print(f"Subtraction: {obj1.Subtraction()}")
print(f"Multiplication: {obj1.Multiplication()}")
print(f"Division: {obj1.Division()}")



obj2 = Numbers()
obj2.Accept()
print(f"Addition: {obj2.Addition()}")
print(f"Subtraction: {obj2.Subtraction()}")
print(f"Multiplication: {obj2.Multiplication()}")
print(f"Division: {obj2.Division()}")
