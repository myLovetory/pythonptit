import math

def ngto(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n > 1
for t in range(int(input())):
    n = int(input())
    dem = 0
    for i in range(1,n):
        if math.gcd(n,i) == 1:
            dem = dem + 1
    if ngto(dem):
        print('YES')
    else:
        print('NO')