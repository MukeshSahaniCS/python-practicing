li = [1,2,3,4]

def double(num):
    return num*2
double_list = list(map(double,li))
print(double_list)

def checkEven(num):
    return num % 2==0
even_li = list(filter(checkEven,li))
print(even_li)

from functools import reduce
def mul(a,b):
    return a*b

result = reduce(mul,li)
print(result)