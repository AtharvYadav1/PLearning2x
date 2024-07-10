def freq_words(str1):
    l1 = str1.split()
    d={}
    for i in l1:
        if i not in d.keys():
            d[i]=0
        d[i]= d[i]+1
    print(d)

freq_words("Hello mate how are you ? I am good mate .")









def freq_word(str):
    l1= str.split()
    d1={}
    for i in l1:
        if i not in d1.keys():
            d1[i]= 0
        d1[i]= d1[i]+1
    d1.pop('.')
    del(d1['?'])
    print(d1)


freq_words("Hello mate how are you ? I am good mate . you you you")



