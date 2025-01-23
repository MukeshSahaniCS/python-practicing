row = int(input("Enter rows  "))

for i in range(row):
    for j in range(i+1):
        print('*',end="")
    for j in range(i,row-1):
        print(' ',end="")
    for j in range(i,row-1):
        print(' ',end="")
    for j in range(i+1):
        print('*',end="")
    print()
for i in range(row):
    for j in range(i,row-1):
        print('*',end="")
    for j in range(i+1):
        print(' ',end="")
    for j in range(i+1):
        print(' ',end="")
    
    for j in range(i, row-1):
        print('*',end="")
    print()