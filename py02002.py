fibo = [1] * 93
for i in range(3,93):
    fibo[i] = fibo[i-1] + fibo[i-2]

for t in range(int(input())):
    a,b = [int(i) for i in input().split()]
    for i in range(a,b+1):
        print(fibo[i] ,end = ' ')
    print()