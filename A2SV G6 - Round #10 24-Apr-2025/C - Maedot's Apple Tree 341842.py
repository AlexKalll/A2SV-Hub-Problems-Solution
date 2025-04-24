# Problem: C - Maedot's Apple Tree - https://codeforces.com/gym/602812/problem/C

t = int(input())

for _ in range(t):
    n = int(input())
    
    adj_list = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    fall_ways = [0 for _ in range(n + 1)]
    
    def dfs(start):
        stack = [(start, -1, 0)]
        visited = [False] * (n + 1)
        visited[start] = True
        
        while stack:
            curr, parent, state = stack.pop()
            
            if state == 1:
                is_leaf = True
                for nbr in adj_list[curr]:
                    if nbr != parent:
                        is_leaf = False
                        fall_ways[curr] += fall_ways[nbr]
                
                if is_leaf:
                    fall_ways[curr] = 1
                
                continue
            
            stack.append((curr, parent, 1))
            
            for nbr in adj_list[curr]:
                if not visited[nbr]:
                    stack.append((nbr, curr, 0))
                    visited[nbr] = True
    
    dfs(1)

    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        print(fall_ways[a] * fall_ways[b])
