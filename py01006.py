def check(str):
    for i in range(len(str)):
        if str[i] != '4' and str[i] != '7':
            return 'NO'
    return 'YES'
for t in range(int(input())):
    str = input()
    print(check(str))
    
                    
    