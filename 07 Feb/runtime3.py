def common_char(str1, str2):
    s1 = set(str1)
    l1= list(str1)
    l1_space = str1.split(' ')
    print (l1)
    print (l1_space)
    s2 = set(str2)
    common = s1 & s2
    c = str(common)
    all = s1 | s2
    l = list(all)
    z = zip(common, all)
    d= dict(z)
    print(f"common chars are {common} and all chars are {all} and {c} and {d}")


#find common string
st1 = input("enter first ir ir ir: ")
print('count', st1.count('ir'))
st2 = input("enter second : ")
common_char(st1, st2)