# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        count = defaultdict(int)

        for u, v in edges: # traverse over the graph
            count[v] += 1

        ans, parentCount = 0, 0
        for i in range(n):
            if not count[i]:
                ans = i
                parentCount += 1
            if parentCount == 2:
                return -1
        return ans