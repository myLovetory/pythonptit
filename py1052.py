import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i==0:
            return False
    return True
for t in range(int(input())):
    s = int(sum(int(i) for i in input()))
    if isPrime(s):
        print('YES')
    else:
        print('NO')