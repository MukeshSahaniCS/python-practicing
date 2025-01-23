row = int(input("enter number of rows"))
#col = int(input("enter number of columns"))

for i in range(row):
    for j in range(i+1):
        print('*',end=" ")
    print()