def decor(func):
    def inner(name):
        if name == 'Ayush':
            print(name, " is Learning Java")
        else:
            func(name)
    return inner

@decor
def choice(name):
    print(name, " is Learning Python")

choice("Akash")
choice("Ayush")
choice("Neha")

def smartDiv(func):
    def inner(a,b):
        if b==0:
            print('B should not be 0.')
        else:
            func(a,b)
    return inner

@smartDiv
def div(a,b):
    print('Division is: ',a/b)

div(10,2)
div(10,0)

def repeat(num):
    def outer(func):
        def inner():
            for i in range(num):
                func()
        return inner
    return outer

@repeat(num = 3)
def msg():
    print("Hello")

msg()