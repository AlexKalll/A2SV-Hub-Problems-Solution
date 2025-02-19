# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    char_set = set(s)
    ans = float('inf')

    for cand in char_set:
        left = 0
        right = len(s) - 1
        count = 0

        while left < right:
            if s[left] != s[right]:
                if cand == s[left]:
                    count += 1
                    left += 1
                elif cand == s[right]:
                    count += 1
                    right -= 1
                else:
                    count = -1
                    break
            else:
                left += 1
                right -= 1
            
        if count != -1:
            ans = min(ans, count)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)