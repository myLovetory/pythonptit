import math

def isprime(n):
    if n < 5:
        return False
    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    if not isprime(int(s)) or not isprime(int(s[::-1])):
        return False
    elif s == s[::-1]:
        return False
    return True
def dao(n):
    # Chuyển số thành chuỗi
    s = str(n)
    
    # Đảo ngược chuỗi
    reversed_s = s[::-1]
    
    # Chuyển chuỗi đảo ngược thành số
    reversed_n = int(reversed_s)
    
    return reversed_n
    
for t in range(int(input())):
    n = int(input())
    for i in range(2, n):
        if check(str(i)) and dao(i) < n:
            print(i, end=" ")
    print()