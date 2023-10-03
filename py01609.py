#gojo satoru = 1 / 2
n = 0
khoitao = ['2', '3', '5', '7']
kqua = []

def check(s) :
    if s[-1] == '2' : return False
    check = [0] * 4
    for i in s :
        for j in range(4) :
            if i == khoitao[j] : check[j] = 1
    if sum(check) == 4 : return True
    return False

def Try(k, s) :
    if k >= 4 :
        if check(s) : kqua.append(s)
    if k == n :
        return
    for i in range(4) :
        Try(k+1, s+khoitao[i])

n = int(input())
Try(0, '')
c = sorted(kqua, key = lambda x : len(x))
for i in c :
    print(i)
    