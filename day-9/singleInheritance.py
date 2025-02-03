class Demo:
    def disp(self):
        print("Inside display One")

class Demo2(Demo):
    pass

d2 = Demo2()
d2.disp()
