'''
Công thức lãi suất kép = P*(1+r/n)^n*t, 
trong đó: 
- P = số tiền gốc (số tiền đầu tư ban đầu). 
- r = lãi suất danh nghĩa hàng năm. 
- n = số lần tiền lãi được nhập gốc mỗi năm
trong ctrinh thì 
m = n * (1 + x%) ^ năm
==> năm = log(m/n) cơ số 1+x/100
'''
import math
for i in range(int(input())):
    
    n,x,m = [float(x) for x in input().split()]
    
    kqua = math.log(m/n , 1 + x/100)
    #ham ceil de lam tron
    print(math.ceil(kqua))
