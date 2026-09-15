friends=["Orange", "Apple", 3, 4.5, False, "Moon", "Jahan"]
print(friends)
friends.append("Something add")
print(friends)

list1=[1, 23, 4, 76, 7, 99]

print(list1)
# list1.sort() #sort mean serial e sajano
# list1.insert(4, 66) #insert mean place change kore 
# list1.reverse() #reverse mean pison theke samne ana
# list1.pop(4) #pop meaning j kono list item remove kora
list1.remove(76)
print(list1)
print(type(list1))

stu = ["Laboni", "Ratul", "Samia", "Harry", "Oishi", "Masiha"]

stu.append("JEFFY")         #append means add somenthing at the last of list
stu.insert(2, "Jeffy")      #insert index e bose
print(stu)
stu.remove("Ratul")     #kono item remove korar jonno remove method use kora hoy
stu.pop(5)          #pop() faka thakle last item remove kore
                    #pop index diyeo kora jay
print(stu)


roll = [1, 7, 0, 2, 9]
roll[2] = roll[4]           #roll er modde e index k 4 index k replace kore
print(roll)
roll.sort()
print(roll)
roll.extend(stu)            # extend e koyekta list add kra jabe
print("After Extend:", roll)
