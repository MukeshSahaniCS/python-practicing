'''
 : List Comprehension:-
 Syntax ->
 [expression for i in iterable object condition]
'''

li = [1,2,3,4,5]
# sqlist = []
# for i in li:
#     sqlist.append(i**2)
# print(sqlist)

new_li = [i for i in li] # copying the list
print(new_li)

sq_li = [i**2 for i in li] # square of list of eke
print(sq_li)

even_list = [i for i in li if i%2==0]
print(even_list)

even_odd = ['even' if i%2==0 else 'odd' for i in li]
print(even_odd)

# nested for loop inside list comprehesion

li1 = [[10,20],[30,40],[50,60]]

new_lis = [ele for i in li1 for ele in i]
print(new_lis)

r1= 1
r2=1
r3=1
sum=2

tup = [[i,j,k] for i in range(r1+1) for j in range(r2+1) for k in range(r3+1) if (i+j+k) != 2]
print(tup)