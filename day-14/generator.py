def disp():
    return 10 
    print("Instruction")
    return 20
    return 30
# print(disp())
# print(disp())
# print(disp())

def generator():
    print("Hello")
    yield 10
    yield 20
    yield 30

gen = generator()  # Create a single generator instance

# print(next(gen))  # Yields 10
# print(next(gen))  # Yields 20
# print(next(gen))  # Yields 30

# def fibonacci(num):
#     a,b=0,1
#     for i in range(num):
#         print(a)
#         a,b=b,a+b
# fibonacci(10)

def fibonacci_gen(num):
    a,b=0,1
    for i in range(num):
        yield a
        a,b=b,a+b
ref = fibonacci_gen(1000)

print(next(ref))
print(next(ref))
print(ref.__next__())
