for t in range(int(input())):
    s  = input()
    kqua = 1
    for i in s:
        if int(i) != 0:
            kqua = int(i) * kqua
    print(kqua)
    