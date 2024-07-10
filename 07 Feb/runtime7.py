l1= [1,1,3,4,5,6]
l2=["a",'b','c','d','e','f']
dict_l = {key:value for (key,value) in zip(l1,l2)}
print(dict_l)


#logic2
d={}
for ke in l1:
    for val in l2:
        d[ke]=val
        l2.remove(val)
        break
print(d)

#logic3
l1= [1,1,3,4,5,6]
l3=["a",'b','c','d','e','f']

dic2=dict(zip(l1,l3))
print(dic2)

