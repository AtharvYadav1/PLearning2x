def map_rno(keys,values):
    d = zip(keys,values)
    p= dict(d)

    print(p)

    d2={}
    for key in keys:
        for value in values:
            d2[key]=value
            values.remove(value)
            break
    print(d2)


map_rno(["Atharv", "Yadav", "Mani"], [1,2,3,4])