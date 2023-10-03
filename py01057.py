import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True if n > 1 else False
for t in range(int(input())):
    s = input()
    oke = 1
    for i in range(0,len(s)):
        if isPrime(int(s[i])) and not isPrime(i):
            oke = 0
            break
        elif not isPrime(int(s[i])) and isPrime(i):
            oke = 0
            break
    if oke == 1:
        print('YES')
    else: print('NO')
        
