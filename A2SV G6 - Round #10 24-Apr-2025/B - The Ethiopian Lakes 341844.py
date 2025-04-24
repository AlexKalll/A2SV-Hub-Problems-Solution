# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

def dfs(grid, visited, i, j):
    stack = [(i, j)]
    volume = 0
    n, m = len(grid), len(grid[0])
    
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        volume += grid[x][y]
        
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] > 0:
                stack.append((nx, ny))
    
    return volume

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    visited = [[False] * m for _ in range(n)]
    max_volume = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                volume = dfs(grid, visited, i, j)
                max_volume = max(max_volume, volume)
    
    print(max_volume)
