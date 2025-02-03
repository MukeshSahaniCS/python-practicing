
class Add:
    def calculate(self, a, b):
        print('Addition is : ',a+b)
class Sub:
    def calculate(self, a, b):
        print('Subtraction is : ',a-b)
class Mul:
    def calculate(self, a, b):
        print('Multiplication is : ',a*b)

class Div:
    # def calculate(self, a, b):
    #     print('Division is : ',a/b)
    pass


#  Duck Typing
'''
ref wont check the type of object.
ref only give importance to the calculate method.
ref only give importance to the method of object.
'''

def permit(ref,a,b):
    if type(ref).__name__ == "Div":
        print("Div class does not have calculate")
    else:
        ref.calculate(a,b)
permit(Add(),20,40)
permit(Sub(),100,40)
permit(Mul(),2,30)
permit(Div(),30,30)
