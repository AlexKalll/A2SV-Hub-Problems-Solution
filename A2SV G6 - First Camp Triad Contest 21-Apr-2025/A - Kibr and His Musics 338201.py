# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

from collections import defaultdict, Counter
import bisect

def solve():
    # Read the number of items (n) and number of queries (m)
    n, m = map(int, input().split())
    
    # Initialize an array to store the cumulative products
    arr = [0] * n
    
    # Read pairs of (l, r) and compute their products
    for i in range(n):
        l, r = map(int, input().split())
        arr[i] = l * r
    
    # Compute the cumulative sum array
    for i in range(1, n):
        arr[i] += arr[i - 1]
    
    # Read the queries
    queries = list(map(int, input().split()))
    ans = []
    
    # Process each query using binary search
    for q in queries:
        index = bisect.bisect_left(arr, q)
        ans.append(index + 1)  # Convert to 1-based index
    
    return ans

if __name__ == "__main__":
    results = solve()
    for res in results:
        print(res)
