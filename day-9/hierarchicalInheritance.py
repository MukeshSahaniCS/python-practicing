class Demo:
    def disp1(self):
        print("Inside One")
class Demo2(Demo): 
    def disp2(self):
        print("Inside disp2")
class Demo3(Demo):
    pass

d3 = Demo3()
d3.disp1()
d2 = Demo2()
d2.disp1()
d2.disp2()