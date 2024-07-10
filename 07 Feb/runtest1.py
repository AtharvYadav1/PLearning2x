def fun(str1, str2):
    length = len(str1)

    l = list(str1)

    for i in range (2,length+1):
        l1=str1.replace("r", "7")

    list= l
    list.insert(0,str[0])
    str3=''.join(list)
    #print(str3)
    return str3


a =fun('retest','7' )
print(a)
list2=[]
dict3={1:a,4:7}
setr={1,3,7,8,7}
print(type(a))
print(type(list2))
print(type(dict3))
print(type(setr))