#replace Manually
st = 'atharv yadav'

l1 = list(st)
print(l1)
for i in range (1,len(l1)):
    if l1[i] == 'a':
        l1.pop(i)
        l1.insert(i, '*')
print (l1)
st = ''.join(l1)
print(st)