import math
def ngto(n):
    for i in range(2,int(math.sqrt(n))+ 1):
        if n % i == 0:
            return False
    return True
for t in range(int(input())):
    s = input()
    le, nt = len(s),0
    for i in s:
        if ngto(int(i)):
            nt += 1
    print('YES' if ngto(le) and nt > le - nt else 'NO')