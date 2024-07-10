list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

dy = {}
for key in list1:
    for value in list2:
        dy[key] = value
        list2.remove(value)
        break
print(dy)

str2='iNDi    a    '
str='89'
str=str2.strip()
print(str2.startswith("I"))
print(bool)
print (str)

