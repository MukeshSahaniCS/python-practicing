class Student:
    college = "Kodnest"
    def get_info(self):
        print(f"College name is : {Student.college}")
    @classmethod
    def change_name(cls,new_name):
        cls.college=new_name
    
s1 = Student()
s1.get_info()
Student.change_name('Code')
s1.get_info()