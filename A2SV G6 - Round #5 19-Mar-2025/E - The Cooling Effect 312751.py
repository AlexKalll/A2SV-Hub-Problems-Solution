# Problem: E - The Cooling Effect - https://codeforces.com/gym/591928/problem/E

q = int(input())

for _ in range(q):
    n, k = map(int, input().split()) 
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    all = [float('inf')] * n

    for i in range(k):
        all[a[i]-1] = t[i]
    
    
    forward = [float('inf')] * n
    forward[0] = all[0]
    for i in range(1, n ):
        forward[i] = min(forward[i-1] + 1, all[i])

    backward = [float('inf')] * n
    backward[-1] = all[-1]
    for i in range(n-2, -1, -1):
        backward[i] = min(backward[i+1] + 1, all[i])
    
    
    for i in range(n):
        print(min(forward[i], backward[i]),end=" ")
    