for t in range(int(input())):
    sums = str(sum(int(i) for i in input()))
    if len(sums) > 1 and sums == sums[::-1]:
        print('YES')
    else:
        print('NO')