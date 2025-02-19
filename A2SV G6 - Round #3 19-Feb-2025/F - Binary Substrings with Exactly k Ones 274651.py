# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
s = input()
at_most_k = 0
at_most_k_1 = 0
ones_cnt = 0
left = 0

for right in range(len(s)):
    if s[right] == '1':
        ones_cnt += 1
    while ones_cnt > k:
        if s[left] == '1':
            ones_cnt -= 1
        left += 1
    at_most_k += right - left + 1

# the num of subarrays having at most k-1 ones
if k > 0:
    start = 0
    ones_cnt = 0
    for end in range(len(s)):
        if s[end] == '1':
            ones_cnt += 1  
        while ones_cnt > k-1:
            if s[start] == '1':
                ones_cnt -= 1
            start += 1
        at_most_k_1 += end - start + 1
# the difference b/n num of subarrays having at most k ones and at most k-1 ones is the num of subarrays having exactly k ones

print(at_most_k - at_most_k_1)
