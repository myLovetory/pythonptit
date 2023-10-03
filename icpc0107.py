for t in range(int(input())):
    p, q = input().split()
    #tao str nhap chung neu do dai lơn hơn 1 thì có 2 str dc nhap
    strnhap = input().split()
    #kiemtra do dai string
    if len(strnhap) == 1:
        str1 = strnhap[0]
        #nhap str2
        str2 = input()
    else:
        str1, str2 = strnhap
    #num1 thay p bằng q num2 thay q băng p
    num1 = int(str1.replace(p,q)) + int(str2.replace(p,q))
    num2 = int(str1.replace(q,p)) + int(str2.replace(q,p))
    print(min(num1,num2), max(num1,num2))
    
        
        
        
        
    
    