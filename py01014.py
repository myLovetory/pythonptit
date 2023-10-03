a, k, n = [int(i) for i in input().split()]
startarray = (int(a/k)+ 1) *k - a
endarray = int(n / k) * k - a
if startarray <= endarray:
    for i in range(startarray,endarray+1,k):
        print(i,end=' ')
else:
    print(-1)