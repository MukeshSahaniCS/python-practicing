'''
1. In tuple we can store Homogeneous as well as Hetrogeneous Data.
2. In Tuple we can store duplicate values.
3. Tuple is an Ordered Collection of Data: Order of insertion will remain as it is in the outout.
4. Tuple are Immutable : Once we declare the tuple we can not modify it.

'''

tup = (10, 10, 20, 30, 'kodnest', True)
print(tup, type(tup))

print(tup.count(10))
print(tup.index(30))

# tup.append(12)
# tup.remove(10)
# tup.pop()
# del tup[1]

# Delete the tuple
# del tup

# concate tuple
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1 + t2
print(t3)

# Repeating tuple
t4 = ('hi',) * 4
print(t4) #('hi','hi','hi','hi') 

# packing and unpacking
student = ("Ravi", 20, "Physics")
# unpacking
name, age, course =student
print(name)
print(age)
print(course)


# Create a Singleton tuple
# tup = (10) # this is a int data 
tup = (10,)
print(tup, type(tup))