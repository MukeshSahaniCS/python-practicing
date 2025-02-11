def checkAge(age):
    if(age<18):
        raise ValueError('Age is must greater than 18')
try:
    checkAge(12)
except ValueError as e:
    print('Error message: ',e)
