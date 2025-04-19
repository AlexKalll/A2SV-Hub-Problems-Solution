# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

def validate(mid):
    last = "R"
    count = 0
    for i in range(n):
        if penalty[i] > mid:
            if s[i] == "B" and last == "R":
                count += 1
            last = s[i]
    return count <= k

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    penalty = list(map(int,input().split()))

    left = 0
    right = max(penalty)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if validate(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)