'''
1. In list we can store Homogeneous as well as Hetrogeneous Data.
2. In List we can store duplicate values.
3. List is an Ordered Collection of Data: Order of insertion will remain as it is in the outout.
4. List are Mutable : Once we declare the list we can modify it.

'''

li1 = [10, 20, 30, True, 'Kodnest']
print(li1, type(li1))

# append() : Will add element at the end of the list
li1.append(300)
print(li1)

print(li1[0])
print(li1[1])

# insert(index, elem) : 
li1.insert(1,15)
print(li1)

# remove(ele) : Remove the first occ of the specified element
li1.remove(20)
print(li1)

# li1.remove(0) # 0 is not in list Error
# print(li1)

# in and not in operator

print(200 in li1) # False
print('Kodnest' in li1) # True

# pop() : Without argument will delete last ele from list and return last ele
# If specify argument then delete specify index
print(li1.pop())
li1.pop(0)
print(li1)

# delete an item at specific position or entire list.
del li1[0]
print(li1)
del li1
# print(li1) # Delete li1