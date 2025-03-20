# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.minval = float('inf')

        def backtrack(i):
            if i >= len(cookies):
                self.minval = min(self.minval, max(child))
                return
            
            for j in range(k):
                if child[j] + cookies[i] >= self.minval:
                    continue

                child[j] += cookies[i]
                curr = backtrack(i+1)
                child[j] -= cookies[i]
                
                if child[j] == 0:
                    break

        backtrack(0)
    
        return self.minval