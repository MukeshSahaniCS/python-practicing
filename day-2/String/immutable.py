'''
Strings are Immutable:
1.Once we declare the string we cannot modify it, if we try to modify 
the string it will create new string.

2.If new string does not have any reference variable then it will be 
removed.

3.Python Internally uses String Interning.

4.String Interning is the Process of Checking string Intern Pool
before creating any new object.

Whenever we want to create new object, Python first will check string
intern pool, weather that object already exist or not.

When Object already exist in the string intern Records then address
of existing object will be reused.
'''
s1 = 'kodnest'
s1.upper()
print(s1)

s2=s1.upper()
print(s2)

print(s1, id(s1))
print(s2, id(s2))

# mess="Hello"
# new_mess="Hello"

# print(mess, id(mess))
# print(new_mess,id(new_mess))

mess="Hello"
new_mess="World"

print('mess Id of H ',id(mess[0]))
print('mess Id of o ',id(mess[-1]))
print('new_mess Id of W ',id(new_mess[0]))
print('new_mess Id of o ',id(new_mess[1]))
