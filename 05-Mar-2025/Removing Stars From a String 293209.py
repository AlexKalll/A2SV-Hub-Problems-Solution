# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isalnum():
                stack.append(c)
            else:
                stack.pop()
        
        return ''.join(stack)