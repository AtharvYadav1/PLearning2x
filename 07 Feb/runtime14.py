#replace Manually
list = ['1','4','3','8','3','6','9','2']
print(list)
for i in range (len(list)):
    if list[i] == '3':
        list.pop(i)
        list.insert(i, '13')
print (list)