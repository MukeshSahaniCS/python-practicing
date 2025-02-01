'''
Instance Variable : Instance var are such variable which are present specifically to that particular instance only. Which are declared inside the constructor.

Class Variable : Class var are class based variable which are common for all the object for that particular class.

Employee -> Has part name, age designation, company_name
name, age and designation are instance variable 
company_name is Class variable

'''
class Employee:
    company_name = 'Code' 
    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
    def login(self,time):
        print(f'{self.name} logged in at {time}')
    def logout(self,time):
        print(f'{self.name} logged out at {time}')
    def work(self, hours):
        print(f'{self.name} worked for {hours}')
    
    def getDetails(self):
        print('Employee name : ', self.name)
        print('Employee age : ', self.age)
        print('Employee Designation : ', self.designation)

e1 = Employee("Mukesh",21,'SDE')
e2 = Employee("Akash",20,'Development')
e3 = Employee("Prakash",22,'Sales')

e1.getDetails()
e2.getDetails()
e3.getDetails()

