# s = input()
# sub = input()
# cnt = 0

# n=len(s)-len(sub)+1

# for i in range(n):
#     if sub == s[i:len(sub)+i]:
#         cnt+=1
# print(cnt)

s1 = "abc123"
print(s1.isalnum())

s2 = 'mukesh'
print(s2.isalpha())

print('12'.isdigit())

print('mukesh'.islower())
print('mukesh'.isupper())

print(any([True, False, False]))
print(any([False, False, False]))
