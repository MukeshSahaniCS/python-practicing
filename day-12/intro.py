# def disp(a,b):
#     print(a/b)
# disp(10,0)
# disp(10,5)
# disp(20,5)

def disp(a,b):
    try:
        print("Task Started")
        print(a/b)
    except:
        print("Cannot divide by zero")
    else:
        print('Task executed withour any exception')
    finally:
        print("Task Ended")
    
disp(10,0)
disp(10,5)
disp(20,5)