import math

bitch = [0] * 10001
def enthos():
    bitch[0] = bitch[1] = 1
    for i in range(2,int(math.sqrt(10000)) + 1):
        if bitch[i] == 0:
            for j in range(i * i, 10001, i):
                bitch[j] = 1

enthos()
arr = [0]
for i in range(10001):
    if bitch[i] == 0:
        arr = arr + [i]
n, k = [int(x) for x in input().split()]
p = 0
for i in range(n + 1) :
    k += arr[p]
    print(k, end = " ")
    p += 1
    