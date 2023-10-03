import math
for t in range(int(input())):
    a = list(int(i) for i in input())
    tong, tich = 0, 0
    for i in range(len(a)):
        if i % 2 == 0:
            tong += a[i]
        else:
            if a[i] != 0:
                if tich == 0:
                    tich = a[i]
                else:
                    tich *= a[i]
    print(str(tong) + " " + str(tich))
