# Problem: D - Repeating Cipher - https://codeforces.com/gym/585132/problem/D

n = int(input())
t = input()

s = t[0]
i = 0
j = 1
while i < len(t):
    i += j 
    j += 1
    if i < len(t) :
        s += t[i]

print(s)