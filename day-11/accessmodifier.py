'''
Access modifier: To determine  the accessibility of data members and member function

1. Public : It should be accessed inside the class, outside the class 
a = 10

2. Private : It should be accessed inside the same class in which we have declared and inside child class
__b = 20

3. Protected : It should be accessed inside the same class in which we declared.
_c = 30
'''
# Public access modifier
'''
class Demo:
    def __init__(self,name):
        self.name = name
    def disp(self):
        print(self.name)
d = Demo('Akash')
print(d.name)
d.disp()
class Demo1(Demo):
    def disp1(self):
        print(self.name)
d2 = Demo1('Pooja')
print(d2.name)
d2.disp1()
'''
'''
The variables which are public, can be accessed inside the same class, outside of any class, inside the child lass, inside non-child class.
'''

# Protected 
'''class Demo:
    def __init__(self,name):
        self._name = name
    def disp(self):
        print(self._name)
d = Demo('Akash')
print(d._name)
d.disp()
class Demo1(Demo):
    def disp1(self):
        print(self._name)
d2 = Demo1('Pooja')
print(d2._name)
d2.disp1()

class Demo3:
    def disp3(self):
        print(d._name)

d3 = Demo3()
d3.disp3()
'''

'''
The variables which are protected, should be accessed inside the same class, outside of any class, inside the child lass, inside non-child class.
this is programmer duty to follow these rules
'''

# Private

class Demo1:
    def __init__(self, name):
        self.__name = name # Private variable

    def getName(self):
        return self.__name
    def setName(self,newName):
        self.__name = newName

d1 = Demo1('Akash')
# print(d1.__name) #Error
print(d1.getName())
d1.setName('Pooja')
print(d1.getName())