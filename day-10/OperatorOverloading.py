class Demo1:
    def __str__(self):
        return "Hello"
    def __add__(self,other):
        self.a = 20
        other.b = 30
        return (self.a + other.b)

class Demo2:
    def __str__(self):
        return "Hey"

d1 = Demo1()
d2 = Demo2()
'''In Python if we print reference variable then internally Python __str__() which always return string representation of an address of an object. 
Dunder Method : The methods which has suffix and prefix as double underscore(__) These dunder method can be called as Magic method because as programmer we no need to call any methods, automatically methods will be invoked.
 '''
# print(d1+d2)

print(d1)
print(d2)

print(d1+d2)