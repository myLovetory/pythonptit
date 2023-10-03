def zodiac_sign(d, m):
    switcher = {
        1: lambda: "Ma Ket" if d < 20 else "Bao Binh",
        2: lambda: "Bao Binh" if d < 19 else "Song Ngu",
        3: lambda: "Song Ngu" if d < 21 else "Bach Duong",
        4: lambda: "Bach Duong" if d < 20 else "Kim Nguu",
        5: lambda: "Kim Nguu" if d < 21 else "Song Tu",
        6: lambda: "Song Tu" if d < 21 else "Cu Giai",
        7: lambda: "Cu Giai" if d < 23 else "Su Tu",
        8: lambda: "Su Tu" if d < 23 else "Xu Nu",
        9: lambda: "Xu Nu" if d < 23 else "Thien Binh",
        10: lambda: "Thien Binh" if d < 23 else "Thien Yet",
        11: lambda: "Thien Yet" if d < 23 else "Nhan Ma",
        12: lambda: "Nhan Ma" if d < 22 else "Ma Ket"
    }
    return switcher.get(m, lambda: "Invalid month")()

t = int(input())
for i in range(t):
    d, m = [int(x) for x in input().split()]
    result = zodiac_sign(d, m)
    print(result)