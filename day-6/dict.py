'''
1. In Dictionary we can not store duplicate keys but store duplicate values.
2. dictionaries are ordered collections as of Python 3.7 and later. Before Python 3.7, dictionaries were unordered
3. Dictionary are mutable.

'''

d1 = {'name':'Mukesh', 'age':22, 'phone': 988988}

print(d1, type(d1))

# keys, values and items
for i in d1.keys():
    print(i)
for i in d1.values():
    print(i)
for key, val in d1.items():
    print(f'Key : {key} value : {val}')

# adding new key-value

d1['address'] = 'Gorakhpur'
print(d1)

# update an existing value
d1['name'] = 'Pooja'
print(d1)

# removing items from dict

# del d1['address']
# print(d1)

d1.pop('address')
print(d1)