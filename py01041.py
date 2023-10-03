def test(s):
    if len(s) < 3:
        return 'NO'
    arr = list(int(i) for i in s)
    check = True
    for i in range(1,len(arr)):
        #check tang chat
        if check and arr[i] <= arr[i-1]:
            check = False
        elif not check and arr[i] >= arr[i-1]:
            return 'NO'
    return 'YES'
for t in range(int(input())):
    s = input()
    print(test(s))
        