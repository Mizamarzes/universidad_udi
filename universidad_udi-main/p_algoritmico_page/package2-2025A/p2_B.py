y = int(input())

if y%4 == 0:
    if y%100 != 0 or y%400 == 0:
        print("BISIESTO")
    else:
        print("NO BISIESTO")
else:
    print("NO BISIESTO")
        