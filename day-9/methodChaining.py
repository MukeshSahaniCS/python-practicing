'''
Method chaining is the process of calling one method from another method.
'''
class GrandParent:
    def cook(self):
        print("Grandparent can cook Biryani...")
    
class Parent(GrandParent):
    def cook(self):
        print("Parent can cook Maggie...")

class Child(Parent):
    def cook(self):
        print("Child wont cook...")
        super().cook()
        super(Parent,self).cook()

c = Child()
c.cook()