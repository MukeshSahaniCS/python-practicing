def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('ZeroDivisionError Occured and Handled')
    except NameError:
        print('Name Error Occured and Handled')
    except TypeError:
        print('TypeError Occured and Handled')
    except:
        print('Some Error Occured and Handled')
disp(10,0)
disp(10,'a')
disp(20,5)
