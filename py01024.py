
def check(str):
    sum = int(str[0])
    for i in range (1, len(str)):
        
        if abs(int(str[i]) - int(str[i - 1])) != 2:
            return "NO"
        sum += int(str[i])
        if sum % 10 == 0:
            return "YES"
    return "NO"
for i in range(int(input())):
    str = input()
    print(check(str))
    