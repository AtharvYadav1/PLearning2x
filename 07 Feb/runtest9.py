l1 = [1,4,5,6,7,2]
temp = l1[1]
l1[1]=l1[5]
l1.insert(5,temp)
l1.pop(6)
print (l1)