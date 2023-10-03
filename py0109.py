p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    str = input()
    if str[0] =="0":
        break;
    k,s = str.split()
    k = int(k)
    kqua= ""
    for i in s:
        kqua += p[((p.find(i)+k)) % 28]
    print(kqua[::-1])
    