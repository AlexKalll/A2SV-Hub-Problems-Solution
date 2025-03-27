# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

from collections import defaultdict
ht = defaultdict(list)

n = int(input())

for i in range(n-1):
    parent = int(input())
    ht[parent].append(i + 2)

for i in range(1, n + 1):
    leaf_count = 0
    for j in ht[i]:
        if not ht[j]:
            leaf_count += 1

    # print(leaf_count)      
    if leaf_count < 3 and leaf_count > 0:
        print("No")
        break
else:
    print("Yes")