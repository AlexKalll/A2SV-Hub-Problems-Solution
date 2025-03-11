# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

import sys, math
from collections import Counter, defaultdict, deque  
from inspect import currentframe as  cf

input = sys.stdin.readline  
def iinput(): return (int(input()))  
def linput(): return (list(map(int, input().split())))  
def sinput(): return (input().strip())  
def minput(): return (map(int, input().split()))  

t = int(input())
for _ in range(t):

	n = iinput()
	arr = linput()

	cnt = 0
	l = 1
	while l < n:
		if arr[l] < arr[l - 1]:
			cnt +=1 
			l += 1
		l += 1

	print(cnt)	



