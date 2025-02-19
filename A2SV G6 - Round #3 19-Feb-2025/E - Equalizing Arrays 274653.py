# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

i = j = 0
count = 0

while i < n and j < m: 
    if a[i] == b[j]:
        i += 1
        j += 1
        count += 1
    elif a[i] < b[j]:
        if i + 1 < n:
            a[i+1] += a[i]
            i += 1
        else:
            break
    else:
        if j + 1 < m:
            b[j+1] += b[j]
            j += 1
        else:
            break

if count and i == n and j == m:
    print(count)
else:
    print(-1)
    
