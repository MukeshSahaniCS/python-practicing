'''
1. The methods which are inherited from from parent class and was used as it is in child class that is inherited method
2. If you want to changing the implementation of method in child class that is called overriden method
3. The method which is declared in child class only accessible in child class.
'''

class Student:
    def study(self): # inherited method
        print('Student is studying')
    def play(self):
        print("Student is playing cricket")

class Employee(Student):
    def work(self): # child specific method
        print("Employee is working.")
    def play(self): # overriden method
        print("Employee is playing Hockey.")

e = Employee()
e.play()
e.work()
e.study()