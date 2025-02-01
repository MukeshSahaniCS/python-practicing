class Calci:
    # Static method
    @staticmethod
    def add(a, b):
        return a+b
    def cal(self):
        pass
res = Calci.add(4,8)
print(res)

math_op = Calci()
print(math_op.add(10,5))