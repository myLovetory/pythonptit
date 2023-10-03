for i in range(int(input())):
    print("Test ", i + 1, ": ",sep = "",end = "")
    a = sorted(input())
    b = sorted(input())
    if a==b : print('YES')
    else: print('NO')