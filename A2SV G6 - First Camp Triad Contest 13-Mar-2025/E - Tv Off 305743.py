# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

n = int(input())
segments = []
segset = set()

for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r+1))
    segset.add(l)
    segset.add(r+1)
    
seglist = sorted(segset)
# print(listofseg)
segmap = {v:i for i, v in enumerate(seglist)}
# print(segmap)
m = len(seglist)

coverage = [0] * (m+1)
for l, r in segments:
    coverage[segmap[l]] += 1
    coverage[segmap[r]] -= 1
    
for i in range(1, m):
    coverage[i] += coverage[i-1]

pref = [0] * m
for i in range(1, m):
    pref[i] = pref[i-1] + (1 if coverage[i-1] == 1 else 0)
    
for i, (l, r) in enumerate(segments):
    if pref[segmap[r]] - pref[segmap[l]] == 0:
        print(i+1)
        break
else:
    print(-1)