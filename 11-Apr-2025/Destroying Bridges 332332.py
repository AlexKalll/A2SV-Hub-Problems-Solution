# Problem: Destroying Bridges - https://codeforces.com/problemset/problem/1944/A

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if k >= n - 1:
            print(1)
        else:
            print(n)

if __name__ == "__main__":
    main()