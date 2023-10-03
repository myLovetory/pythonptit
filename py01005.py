str = input()
dem = 0
for i in range(len(str)):
    
    if str[i] == '4' or str[i] == '7':
        dem = dem + 1
if dem == 4 or dem == 7:
    print("YES")
else:
    print("NO")