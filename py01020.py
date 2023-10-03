t = int(input())
def check(s1):
    if s1.endswith("86"):
        return "YES"
    return "NO"
while t>0:
    t -= 1
    s = input()
    print(check(s))