def Try(str, n, a, b, c):
    if len(str) == n and a > 0  and a <= b and b <= c:
        print(str)
    if len(str) < n:
        Try(str + 'A', n, a + 1, b, c)
        Try(str + 'B', n, a, b + 1, c)
        Try(str + 'C', n, a, b, c + 1)


n = int(input())
for i in range(3, n + 1):
    Try('', i, 0, 0, 0)