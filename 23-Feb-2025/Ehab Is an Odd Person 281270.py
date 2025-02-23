# Problem: Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
nums= list(map(int, input().split()))

odd = []
even = []
for i, x in enumerate(nums):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

if not odd or not even:
    print(*nums)
else:
    print(*sorted(nums))