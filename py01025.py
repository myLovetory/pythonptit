s = input()

s = s[::-1]
kqua = ""
dem = 0

for i in s:
    if dem == 3:
        kqua += ','
        dem = 0
    kqua += i
    dem += 1

print(kqua[::-1])