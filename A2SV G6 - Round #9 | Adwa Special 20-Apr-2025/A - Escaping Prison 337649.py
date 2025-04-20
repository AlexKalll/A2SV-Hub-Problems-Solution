# Problem: A - Escaping Prison - https://codeforces.com/gym/601269/problem/A

t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    blanket = []
    total_length = 0
    for _ in range(n):
        w, l = map(int, input().split())
        total_length += max(w, l)

    if total_length >= h:
        print("YES")
    else:
        print("NO")