str1 = 'I am a good person'
str2 = 'I am a bad person'
l1_space = str1.split(' ')
l2_space = str2.split(' ')
d= {}

for key in l1_space:
    for val in l2_space:
        d[key] = val
        l2_space.remove(val)
print(d)


d1 = {key1:val1 for (key1,val1) in zip (l1_space, l2_space) }

print (d1)