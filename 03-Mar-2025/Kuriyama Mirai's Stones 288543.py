# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
costs = list(map(int, input().split()))

m = int(input())
queries = []
for _ in range(m):
    type, l , r = map(int, input().split())
    queries.append((type, l, r))

prefix = [costs[0]]
for i in range(1, n):
    prefix.append(prefix[-1] + costs[i])

costs.sort()
sorted_prefix = [costs[0]]
for i in range(1, n):
    sorted_prefix.append(sorted_prefix[-1] + costs[i])

# print(prefix)
# print(sorted_prefix)

for type, l, r in queries:
    if type == 1:
        ans = prefix[r-1] - (prefix[l-2] if l-2 >= 0 else 0)
    else:
        ans = sorted_prefix[r-1] - (sorted_prefix[l-2] if l-2 >= 0 else 0)
    
    print(ans)