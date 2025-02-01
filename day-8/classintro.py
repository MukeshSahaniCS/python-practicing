class Student:
    def learn(self):
        print('Student is learning..')
    def play(self):
        print('Student playing..')

s1 = Student()
s1.learn()
s1.play()

s1.name = 'Mukesh'

print('Name is : ',s1.name)
