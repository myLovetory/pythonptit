for t in range(int(input())):
    s = int(sum(int(i) for i in input()))
    if s % 3 == 0:
        print('YES')
    else:
        print('NO')
