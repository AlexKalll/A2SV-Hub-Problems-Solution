# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        numj = float('-inf')
        nums = reversed(nums)

        for num in nums:
            if num < numj:
                return True
            while stack and num > stack[-1]:
                numj = stack.pop()
                
            stack.append(num)

        return False
