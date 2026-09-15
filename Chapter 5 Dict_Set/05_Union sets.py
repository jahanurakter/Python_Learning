a = {2,4,7,"Maya"}
b = {5,4,7,8}
print(a.union(b))
print(a.intersection(b))
print(b.difference(a))
print(a.symmetric_difference(b))
# print(a.remove(8)) this line gave error
# print(a.discard(6)) repeat none
new_set = a.copy()
print(a)
print(len(b))