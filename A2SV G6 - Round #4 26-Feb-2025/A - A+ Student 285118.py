# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())

    ans = []

    if a <= max(b, c):
        ans.append(max(b, c)-a + 1)
    else:
        ans.append(0)

    if b <= max(a, c):
        ans.append(max(a, c)-b + 1)
    else:
        ans.append(0)

    if c <= max(a, b):
        ans.append(max(a, b)-c + 1)
    else:
        ans.append(0)

    print(' '.join(map(str, ans)))