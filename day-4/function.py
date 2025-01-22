
# Without input and without return statement
def add():
    a = 10
    b = 20
    print("Addition is :  ", a+b)
add()

# With input but without return statement
def sub(a , b):
    print("Subtraction is : ",a-b) 

sub(10,5)

#Without input with return statement

def mul():
    return 10*5

res = mul()
print("Multiplication is : ",res)

# With value and with return statement

def div(a , b):
    return a/b

res = div(10,5)
print("Division is : ",res)