for t in range(int(input())):
    str = input()
    for i in str:
        a = int(str[0:2])
        b = int(str[len(str)-2:len(str)])
    if a==b:
        print('YES')
    else:
        print('NO')