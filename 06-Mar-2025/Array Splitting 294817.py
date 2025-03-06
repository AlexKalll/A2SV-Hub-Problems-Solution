# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

import sys, math
from functools import cmp_to_key
from operator import itemgetter
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
import heapq

input = sys.stdin.readline

def iinput(): return (int(input()))
def linput(): return (list(map(int, input().split())))
def sinput(): return (input().strip())
def minput(): return (map(int, input().split()))

def solve():
    n, k = minput()
    a = linput()
    
    total_sum = 0
    cumulative_sums = []
    
    for i in range(n - 1, -1, -1):
        total_sum += a[i]
        if i > 0:
            cumulative_sums.append(total_sum)
    
    result = total_sum
    cumulative_sums.sort(reverse=True)
    
    for i in range(k - 1):
        result += cumulative_sums[i]
    
    print(result)

def main():
    t = 1
    for _ in range(t):
        solve()
    
if __name__ == "__main__":
    main()