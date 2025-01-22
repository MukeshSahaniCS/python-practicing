'''
1. Conditional : if-else, if-elif
2. Looping : for and while
3. Jumping : break and continue

'''

# def checkAge(age):
#     if(age>=18):
#         print('Eligible for vote')
#     else:
#         print("Not eligible")
# checkAge(19)

# def grade(marks):
#     if(marks>85):
#         print("Grade A")
#     elif(marks<85 and marks>65):
#         print("Grade B")
#     elif(marks<65 and marks>45):
#         print("Grade C")
#     elif(marks<45 and marks>35):
#         print("Grade D")
#     else:
#         print("Grade F")
# grade(76)

# While Loop
# num = 5
# a=1
# while a<=10:
#     print(f'{a} * {num} = ', a*num)
#     a+=1

# for loop
'''
for control_variable in range()

'''
# Iterable object
arr = [10,11,12,13,14]
s = 'mukesh'
d = {'name':'mukesh', 'age':22}

for i in s:
    print(i,end=" ")
print()

for i in arr:
    print(i,end=" ")
print()
for i in d.values():
    print(i,end=" ")
print()
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

for i in range(0,100,25):
    print(i,end=" ")
print()
for i in range(1, 6):
    print(i,end=" ")
print()

for i in range(5): # start default valuemis 0
    print(i,end=" ")
print()
# WAP to print all even number from 1-10

for i in range(1,11):
    if(i%2==0):
        print(i, end=" ")
print()


# Jumping control construct
for i in range(1,11):
    if(i==6):
        continue
    else:
        print(i, end=" ")
print()

for i in range(1,11):
    if(i%7==0):
        break
    else:
        print(i, end=" ")
print()

def disp():
    pass

class Demo:
    pass

for i in range(1,11):
    if(i%2==0):
        pass
    else:
        print(i)