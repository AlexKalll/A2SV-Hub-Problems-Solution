# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(1, len(a)):
        a[i] += a[i-1]
    # print(a)
    for _ in range(q):
        l, r, k = map(int, input().split())
        curr = (r - l + 1) * k 
        if l >= 2:
            total = a[-1] + curr - (a[r-1] - a[l-2])
        else:
            total = a[-1] + curr - (a[r-1])

        if total % 2 != 0:
            print("YES")
        else:
            print("NO")
            

