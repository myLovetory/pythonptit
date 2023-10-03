import math
def check(n):
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1
for t in range(int(input())):
    arr=list(int (i) for i in input())
    dodai , prime = len(arr), 0
    for i in arr:  
        prime += check(i)
    print('YES' if(check(i) and prime > dodai - prime) else 'NO')
    