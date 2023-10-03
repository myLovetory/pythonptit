n = int(input())
list = [int(i) for i in input().split()]
cnt = 0
for i in range(1, len(list)):
    if list[i] != list[i - 1]:
        cnt += 1
print(cnt)