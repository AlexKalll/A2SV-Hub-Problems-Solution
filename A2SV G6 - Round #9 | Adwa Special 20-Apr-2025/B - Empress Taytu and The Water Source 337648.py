# Problem: B - Empress Taytu and The Water Source - https://codeforces.com/gym/601269/problem/B

def check(demands, time, cand, k):
    total = 0
    for i in range(len(demands)):
        trips = (demands[i] + cand - 1) // cand
        total += trips * time[i]
        if total > k:
            return False
    return total <= k

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    left, right = 1, max(d)
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if check(d, a, mid, k):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)