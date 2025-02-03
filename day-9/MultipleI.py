'''class Demo:
    def disp(self):
        print("Inside disp1")

class Demo2():
    def disp(self):
        print("Inside disp2")

class Demo3(Demo, Demo2):
    pass

d = Demo3()
d.disp()'''

# Constructor are inherited in python

class Demo:
    pass

class Demo2():
    def __init__(self):
        self.x = 200

class Demo3(Demo, Demo2):
    pass

d = Demo3()
print(d.x)