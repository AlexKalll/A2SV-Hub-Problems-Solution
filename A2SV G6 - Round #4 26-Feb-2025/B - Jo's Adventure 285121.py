# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
height = list(map(int, input().split()))

query = []
for _ in range(m):
    query.append(list(map(int, input().split())))

pf = [0] * (n)
for i in range(1, n):
    if height[i] < height[i - 1]:
        pf[i] += height[i - 1] - height[i] 
    pf[i] += pf[i - 1]

# print(pf)

pf_back = [0] * (n)
height.reverse()

for i in range(1, len(height)):
    if height[i] < height[i - 1]:
        pf_back[i] += height[i - 1] - height[i] 
    pf_back[i] += pf_back[i - 1]

# print(pf)
# print(pf_back)

for l, r in query:
    if r < l:
        print(pf_back[n - r] - pf_back[n - l])
    else:
        print(pf[r-1] - pf[l-1])


