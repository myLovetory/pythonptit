def Try(s):
    global n, visited
    if len(s) == n:
        print(s)
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            Try(s+str[i])
            visited[i] = 0
str = input()
n = len(str)
visited = [0] * n
Try("")