
num = int(input("Enter number upto which series is required "))
n1=0
n2=1
n3= n2+n1
print(n1)
print(n3)
while(n3 < num):
    n1=n2
    n2=n3
    n3=n2+n1
    if n3 < num:
        print (n3)

