# object.reverse() : will reverse original object
li =[10,5,20,8,40]
print('Before reverse : ',li)

li.reverse()
print('After reverse : ',li)

# reversed(object) : return iterable object 

li2 =[11,6,8,22]
reverse_li=list(reversed(li2))
print(li2)
print(reverse_li)