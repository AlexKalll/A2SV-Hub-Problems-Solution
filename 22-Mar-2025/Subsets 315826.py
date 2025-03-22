# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = []
        combs = []

        def backtrack(i, combs):
            if i == len(nums):
                subs.append(combs.copy())
                return
            
            #inserting
            combs.append(nums[i])
            backtrack(i+1, combs)
            combs.pop()

            # not inserting
            backtrack(i+1, combs)
        
        backtrack(0, combs)
        return subs