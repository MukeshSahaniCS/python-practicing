'''
1. In Set we can store Homogeneous as well as Hetrogeneous Data.
2. In Set we can not store duplicate values.
3. Set is an Unordered Collection of Data: Set does not support indexing
4. Set are mutable.

'''

s1 = {10,True, 'Kodnest', 10,20,32.09}
print(s1, type(s1))

# creating set using set() function

num = set({1,2,3,4,5,6})
print(num)

# add() :Used to add an element in the set
s1.add(200)
print(s1)

# remove() : remove an specific ele
s1.remove(32.09)
print(s1)
# pop() : Without index will delete and return ele
s1.pop()
print(s1)

# delete entire set
del s1

# Union and intersection

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)
s4 = s1.intersection(s2)
print(s4)