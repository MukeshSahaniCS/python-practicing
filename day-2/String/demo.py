s1 = "I'm Mukesh"
s2 = 'My "age" is 22'
s3 = """I am learning 
        Python"""
s4 = '''I am learning 
       string'''

print(s1)
print(s2)
print(s3)
print(s4)

name = "muKEsh"
print(name[0]) # m
print(name[1]) # u
print(name[-1]) # h
print(name[:6]) # mukesh
print(name[0:]) # mukesh
print(name[0:6:2]) # mks

# function in string

print(len(name)) # 6
print(name.endswith("esh")) # True

print(name.count("s")) # 1
print(name.capitalize()) # Mukesh

print(name.lower())
print(name.upper())

text = "Learning Python is fun"
print(text.find("Python"))
print("fun" in text)

# text = text.replace("Python", "Java")

# text.replace("Python", "Java") not change permanently create one string

print(text.replace("Python", "Java"))


string = "apple,banana,cherry"
fruits = string.split(",")
print(fruits)

joined_text = " - ".join(fruits)

print(joined_text)