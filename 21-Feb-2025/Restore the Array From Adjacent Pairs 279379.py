# Problem: Restore the Array From Adjacent Pairs - https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        
        for x, y in adjacentPairs:
            graph[x].add(y)
            graph[y].add(x)
        
        root = None
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break

        visited = set([root])
        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, node, ans)

        ans = []
        dfs(root, None, ans)
        return ans