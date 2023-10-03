t = int(input())
for i in range(t):
    a = list(int(i) for  i in input())
    #scan from last to begin 
    for i in range(len(a) - 1,0,-1):
        #check duoi 5
        if a[i] >= 5:
            a[i-1] = a[i-1] + 1
        a[i] = 0
        #check lam tron
        if a[0] == 10:
            a[0] = 0
            a = [1] + a
    for i in a:
        print(i, end='')
    print()  