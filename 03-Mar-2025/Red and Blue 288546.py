# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    reds = list(map(int, input().split()))
    m = int(input())
    blues = list(map(int, input().split()))

    # keep tracking the maximum possible prefix sum of the red sequences 
    curr_sum = 0
    max_red = 0
    for i in range(n):
        curr_sum += reds[i]
        max_red = max(max_red, curr_sum)

    # find the max possible prefix sum of the blues 
    curr_sum = 0
    max_blue = 0
    
    for i in range(m):
        curr_sum += blues[i]
        max_blue = max(max_blue, curr_sum)

    print(max_red + max_blue)
