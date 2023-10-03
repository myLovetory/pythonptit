str = input()
demhoa = 0
demthuong = 0
for i in str:
    if i >= 'a' and i <='z':
        demthuong = demthuong + 1
    else:
        if i>='A' and i<='Z': 
            demhoa = demhoa + 1
if(demhoa > demthuong):
    strhoa = str.upper()
    print(strhoa)
else:
    strthuong = str.lower()
    print(strthuong)