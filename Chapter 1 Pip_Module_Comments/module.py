#module is a python file, from module we can import a function variable and code
#2 type of module in python (i). Built in module (ii).External module


import pyjokes    #here pyjokes is a programm/code that print jokes

# print("Nothing")
print("Printing jokes")
joke= pyjokes.get_joke()        #here get_jok is a function that generate a joke
print (joke)