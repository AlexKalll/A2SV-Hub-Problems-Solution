# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))

mon_inc = deque()
mon_dec = deque()
l = 0
count = 0

for r in range(n):
    while mon_inc and nums[mon_inc[-1]] < nums[r]:
        mon_inc.pop()
    while mon_dec and nums[mon_dec[-1]] > nums[r]:
        mon_dec.pop()
    mon_inc.append(r)
    mon_dec.append(r)

    while nums[mon_inc[0]] - nums[mon_dec[0]] > k:
        if nums[l] == nums[mon_dec[0]]:
            mon_dec.popleft()
        if nums[l] == nums[mon_inc[0]]:
            mon_inc.popleft()
        
        l += 1
    
    count += r - l + 1

print(count)  
