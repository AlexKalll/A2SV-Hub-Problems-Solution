# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans, stack = [], []

        for i, char in enumerate(pattern + "I", 1):
            stack.append(str(i))

            if char == "I":
                ans += stack[::-1]
                stack = []
            
        return "".join(ans)