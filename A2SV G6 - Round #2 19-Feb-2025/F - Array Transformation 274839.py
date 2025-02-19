# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    hT = Counter(arr)
    freq = list(hT.values())

    freqOffreq = Counter(freq)
    

    ans = float('inf')

    for key in freqOffreq:
        # Calculate the cost of making all frequencies equal to `key`
        curr_cost = 0
        for f in freqOffreq:
            if f >= key:
                curr_cost += ((f - key) * freqOffreq[f])
            else:
                curr_cost += ((f) * freqOffreq[f])

        ans = min(ans, curr_cost)

    print(ans)