for t in range(int(input())):
    s = input()
    n = input()
    l, tontai, dem = len(n), s.find(n), 0
    while tontai != -1:
        dem += 1
        tontai = s.find(n, tontai + l)
    print(dem)