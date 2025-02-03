class GrandParent:
    def __init__(self):
        self.x = 100
    
class Parent(GrandParent):
    def __init__(self):
        self.y = 200
        super().__init__()

class Child(Parent):
    def __init__(self):
        self.z = 300
        super().__init__()

'''
1. Constructor chaining is the process of calling one constructor from another constructor.
2. 
'''

c = Child()
print(c.z)
print(c.y)
print(c.x)