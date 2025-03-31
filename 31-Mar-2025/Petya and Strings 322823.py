# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

li = list(input())
li1 = list(input())
res = 0
for i in range(len(li)):
    if ord(li[i].lower()) < ord(li1[i].lower()):
        res = -1
        break
    elif ord(li[i].lower()) > ord(li1[i].lower()):
        res = 1
        break
if res == 0:
    print(0)
else:
    print(res)