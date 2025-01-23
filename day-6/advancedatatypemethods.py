'''
iterable Object:
list() -> list(iterable object) accept parameter as a iterable object
list(set({10,20})) ->[10,20]
list(tuple(10,20)) ->[10,20]
list(dict()) ->stores only keys in list
list('string') -> ['s','t','r','i','n','g']
list(range(1,5)) -> [1,2,3,4]
'''

# list(iterable object)
# li = list(12) # not iterable obj
# li = list(12.98) # not iterable obj
li = list('mukesh')
print(li)

li2 = list((10,20))
print(li2)

li3 = list({100,200})
print(li3)

li4 = list({'name':'mukesh','age':22})
print(li4) # ['name', 'age']

li5 = list(range(1,11))
print(li5) #[1,2,3,4,5,6,7,8,9,10]

'''
tuple(iterable object)

'''
print('-------------------------------------------------')
tup1 = tuple([10,20,30])
tup2 = tuple({100,200})
tup3 = tuple({'name':'mukesh','age':22})
tup4 = tuple(range(1,5))
tup5 = tuple('mukesh')

print(tup1) #(10,20,30)
print(tup2) #(200,100)
print(tup3) #('name','age')
print(tup4)
print(tup5)

'''
set(iterable object)

'''

s1 = set([10,20,20,30]) 
s2 = set((1,2,3,4))
s3 = set({'name':'mukesh','age':22})
s4 = set(range(1,5))
s5 = set('Mukesh')
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

'''
dict(iterable object)

'''

d1 = dict([['name','mukesh'],['age',22]])
print(d1)