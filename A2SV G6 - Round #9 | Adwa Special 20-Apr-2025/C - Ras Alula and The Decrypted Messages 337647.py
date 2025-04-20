# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C


def can_(s, w):
    w_count = sum(ord(c) for c in w)
    s_count = sum(ord(c) for c in s[:m])
    
    for i in range(m, n):
        if s_count == w_count:
            print("YES")
            return
        s_count += ord(s[i]) 
        s_count -= ord(s[i-m])
        
    if s_count == w_count:
        print("YES")
        return

    print("NO")

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()
    w = input()

    can_(s, w)