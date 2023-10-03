def Try(i, length):
    global n,k
    # check len to hop
    if len(length) == k:
        #hamf print de in ca chi so ma khoong can[]
        print(*length)
        return
    for j in range(i,n):
        Try(j+1, length + [list[j]])
n, k = [int(i) for i in input().split()]
list = sorted(list({int(i) for i in input().split()}))
n = len(list)


Try(0, [])       
        
    
