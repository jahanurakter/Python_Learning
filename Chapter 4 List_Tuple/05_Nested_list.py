a = [[1,3,5,6,7],[4,6,8,9,4],[5,9,3,5,8]]

print(a[1])         #nested list  means list er modde list
print(a[1][2])      # a er 1number list and er 2number index print hbe

colum=[]
for row in a:
    colum.append(row[3])        #akhane row er modde loop giye bar bar index 3 k print korbe
print(colum)
print("4th colum:",colum)