class Employee:
    def __init__(self):
        pass
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print(self.name," is working...")

e1 = Employee('Mukesh',22)
e1.work()

e2 = Employee()
e2.name ="Shyam"
e2.work()