year = int(input("Enter Year:"))
print(year)

if year % 4 == 0:
    if year % 400 == 0:
        print("Leap Year")
    elif year % 100 == 0:
        print("Not a Leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")
