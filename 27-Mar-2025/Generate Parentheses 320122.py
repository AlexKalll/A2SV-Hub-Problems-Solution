# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr, open_count, close_count):
            if len(curr) == 2*n:
                ans.append(''.join(curr))
                return 
            
            if open_count < n:
                curr.append('(')
                backtrack(curr, open_count + 1, close_count)
                curr.pop()

            if close_count < open_count:
                curr.append(')')
                backtrack(curr, open_count , close_count+ 1)
                curr.pop() 
        
        backtrack([], 0, 0)
        return ans 