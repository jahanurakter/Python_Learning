# write a python program to print the contents of directory using the OS module
import os           #os is a built in python module

directory_path = "/Pyhton Learning"     #select the directory path of disk

x = os.listdir(directory_path)          
print(x)

for item in x:
    print(x)
