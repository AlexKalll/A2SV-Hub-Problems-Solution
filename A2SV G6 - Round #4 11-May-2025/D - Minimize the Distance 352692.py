# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

"""
n = int(input())
x = list(map(int, input().split()))

x.sort()

if n %2 == 0:
    print(x[(n-1)//2])
else: 
    print(x[n//2])
"""
    
# n = int(input())
# x = list(map(int, input().split()))

# x.sort()
# print(x[(n-1)//2])

"""
https://codeforces.com/contest/710/problem/B

"""
"""
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

pre = []
p = 0
for i in range(n):
    x = arr[i]
    curr = i*x - p
    pre.append(curr)
    p += x

suff = []
s = 0
for i in range(n - 1, -1, -1):
    x = arr[i]
    curr = -(n - i - 1)*x + s
    suff.append(curr)
    s += x

suff.reverse()

res = [float("inf"), float("inf")]
for i in range(n):
    x = arr[i]
    curr = suff[i] + pre[i]
    if curr < res[1]:
        res = [x, curr]

print(res[0])
"""

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

pref = [nums[0]]

for i in range(1, n):
    pref.append(pref[-1] + nums[i])

smallest = float('inf')
for i in range(n):
    x = nums[i]
    left_dis = (i+1)*x - pref[i]
    right_dis = pref[-1] - (x * (n-i-1)) - pref[i]

    curr = left_dis + right_dis

    if curr < smallest:
        smallest = curr
        ans = nums[i]

print(ans)
