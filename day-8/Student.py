class Student:
    def __init__(self,name, roll_num, grade):
        self.name=name
        self.roll_num = roll_num
        self.grade = grade
    def display_info(self):
        print(f'Name: {self.name}, Roll Number: {self.roll_num}, Grade: {self.grade}')
    def update_grade(self, new_grade):
        self.grade =new_grade
        print(f"{self.name}'s grade has been updated to {new_grade}")
st = Student('Amit','S123','B')
st.display_info()
st.update_grade('A')
st.display_info()