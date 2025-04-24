# Problem: C - Daniel and Computer Game - https://codeforces.com/gym/604781/problem/C

from collections import deque

n, k = map(int, input().split())
left = input()
right = input()

visited = [[False, False] for _ in range(n)]


q = deque()
q.append((0, 0, 0)) 
visited[0][0] = True

while q:
    pos, wall, time = q.popleft()
    
    if pos < time:
        continue

    for new_pos, new_wall in [
        (pos + 1, wall),                    
        (pos - 1, wall),                    
        (pos + k, 1 - wall)                 
    ]:
        if new_pos >= n:
            print("YES")
            exit()
        if new_pos < 0 or visited[new_pos][new_wall]:
            continue
        if new_pos >= time + 1:
            if (new_wall == 0 and left[new_pos] == '-') or (new_wall == 1 and right[new_pos] == '-'):
                visited[new_pos][new_wall] = True
                q.append((new_pos, new_wall, time + 1))

print("NO")
