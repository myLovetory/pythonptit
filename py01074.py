def findMinDivisor():
    global prime
    for i in range(2, int(N ** 0.5) + 1):
        if prime[i] == 0:
            for j in range(i * i, N + 1, i):
                if prime[j] == 0:
                    prime[j] = i
    for i in range(2, N + 1):
        if prime[i] == 0:
            prime[i] = i

def calculate(n):
    if prime[n] == 0:
        return n
    sum = 0
    while n != 1:
        sum += prime[n]
        n //= prime[n]
    return sum

N = int(2e6)
prime = [0] * (N + 5)
findMinDivisor()

n = int(input())
sum = 0
for _ in range(n):
    x = int(input())
    sum += calculate(x)

print(sum)