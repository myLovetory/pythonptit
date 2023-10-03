def solve(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        dao = int(str(n)[::-1])
        n += dao
    return -1


for t in range(int(input())):
    n = int(input())
    print(solve(n))