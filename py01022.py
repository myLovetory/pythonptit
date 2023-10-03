def tach(s) :
    n = 0
    for i in s : 
        n += ord(i) - ord('0')
    return str(n)

s = input()
sum = 0
while(len(s) > 1) :
    s = tach(s)
    sum += 1
print(sum)