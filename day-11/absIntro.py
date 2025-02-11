from abc import ABC, abstractmethod
class Demo(ABC):
    pass
    
d = Demo()

class Demo1(ABC):
    def disp2(self):
        print('Inside disp2')

d1 = Demo1()
d1.disp2()

class Demo2(ABC):
    def info(self):
        print('Inside info')
    @abstractmethod
    def disp3(self):
        print('Inside disp3')

class Demo3(Demo2):
    pass
# d3 = Demo3() # error

'''
-> If abstract class does not have any method then object for that abstract class can be created.
-> If abstract class have only concrete method then object for that abstract class can be created and concrete methods can be invoked.
-> 

'''

class Demo4(ABC):
    @abstractmethod
    def disp(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Demo5(Demo4):
    def disp(self):
        print("Disp")
    def disp2(self):
        print("Inside disp2")
d5 = Demo5()
d5.disp2()