# String functions are built-in methods used to perform operations 
# - on strings in Python.

name = "jahanur akter"

print(len(name))            #returns the length of string  
print(name.endswith("nur"))     #if given ending str is true. ouptput will be show
print(name.startswith("ha"))    #if given str is false. output will be false  
print(name.startswith("ja"))    #givem value is true. 
print(name.capitalize())     
print(name.upper())
print(name.title())


print(f"My name is {name.title()}")     
#f is used before a string to insert variables inside the string using {}.


# len() → Length
# upper() → Uppercase
# lower() → Lowercase
# capitalize() → First letter capital
# title() → Every word capital
# strip() → Remove extra spaces
# replace() → Replace text
# split() → String → List
# find() → Find position
# count() → Count occurrences
# startswith() → Check beginning
# endswith() → Check ending