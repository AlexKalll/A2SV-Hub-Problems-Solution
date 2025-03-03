# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict

n = int(input())

ht = defaultdict(int)
for _ in range(n):
    b, d = map(int, input().split())
    ht[b] += 1
    ht[d] -= 1
# print(years)

ht = dict(sorted(ht.items()))

# print(ht)

ans = 0
idx = 0
pf= 0

for key in ht:
    pf += ht[key]

    if pf > ans:
        ans = pf
        idx = key

print(idx, ans)