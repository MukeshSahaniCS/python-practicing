class Demo:
    def __init__(self):
        self.x = 100
    def __init__(self):
        self.x = 200
    def __init__(self): # last constructor is consider python not support method oveloading and  constructor overloading
        self.x = 300 

d = Demo()
print(d.x)
'''
When we create multiple Constructors in same class then only last declared constructor will  be invoked at the time of object creation.
'''