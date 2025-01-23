# list[start:end:steps]
li = [10,20,30,40,50,60]


sublist = li[0:4:1]
print(sublist)

sublist2 = li[::]
print(sublist2)

sublist3 = li[1::]
print(sublist3)

sublist4 = li[::2]
print(sublist4)

sublist5 = li[::-1] # reverse list
print(sublist5)
sublist6 = li[-1::] # last element
print(sublist6)