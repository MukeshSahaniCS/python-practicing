file = open("test.txt","a")
#print(file.read())
# data = file.read()
# print(data)
# print(data[0])

# firstline = file.readline()
# print(firstline)

# file.write("This is nice")
# file.write("This is nice")


with open('test.txt','r') as file:
    text=file.read()
    print(text)