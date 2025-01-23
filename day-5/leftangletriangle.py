row = int(input("enter number of rows"))

for i in range(row):
    for j in range(i, row):
        print('*',end=" ")
    print()