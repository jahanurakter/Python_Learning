# Negative indexing accesses a string in reverse order, 
# where the last character has index -1.

name = "Maya Rahaman"

print(name[0:2])

print(name[-3: -2])

print(name[2:3])

print(name[:3]) #is same as print (name)[0:3]

print(name[1:]) #is same is print (name[1:5]) 

print(name[1:5])

b = "abcdefghijklmnopqrstuvwxyz"
print(b[1:6:2])                      #string_slicing[start : stop : step]
