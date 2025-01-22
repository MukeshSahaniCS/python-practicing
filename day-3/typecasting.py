#If string is hold integer then it can be converted into int
a = '30'
b = int(a)
print(a, type(a))
print(b, type(b))

# If string is hold string then it can not allow to convert
# c = 'kod'
# d = int(c)
# print(c, type(c))
# print(d, type(d))

# p = float(input("Enter a float number"))
# print(p, type(p))

# bool

q = 12 # 0 and empty string get False
q=bool(q)
print(q,type(q)) # True bool

s = 22.32
s=int(s)
print(s, type(s))

# Error
# u = '32.32'
# u = int(u)
# print(u, type(u))

u =int(float(input("Enter number")))
print(u, type(u))
