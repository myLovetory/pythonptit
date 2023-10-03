for t in range(int(input())):
    n,p =[int(x) for x in input().split()]
    dem = 0
    for i in range(2, n + 1):
        while i % p==0:
            i/=p
            dem += 1
    print(dem)