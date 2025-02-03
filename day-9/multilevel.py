class Demo:
    def disp1(self):
        print("Inside disp1")

class Demo2(Demo):
    def disp2(self):
        print("Inside disp2")

class Demo3(Demo2):
    pass

d3=Demo3()
d3.disp1()
d3.disp2()
