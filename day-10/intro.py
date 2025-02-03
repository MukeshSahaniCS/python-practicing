'''
   <--- Polymorphism --->
Polymorphism is the process in which if something which exihibist many form there we are achieving polymorphism. For ex. -
1. Duck Typing
2. Method Overriding
3. Method Overloading (Simulated)
4. Operator Overloading
'''


# Method Overriding: Inthis code we are achivieng polymorphism using Method Overriding
class Calculator:
    def calculate(self,a,b):
        print("Calculate result of a and b")

class Add(Calculator):
    def calculate(self, a, b):
        print('Addition is : ',a+b)
class Sub(Calculator):
    def calculate(self, a, b):
        print('Subtraction is : ',a-b)
class Mul(Calculator):
    def calculate(self, a, b):
        print('Multiplication is : ',a*b)

class Div(Calculator):
    # def calculate(self, a, b):
    #     print('Division is : ',a/b)
    pass

ref = Add()
ref.calculate(10,20)
ref = Sub()
ref.calculate(30,20)
ref = Mul()
ref.calculate(10,2)
ref = Div()
ref.calculate(10,2)
