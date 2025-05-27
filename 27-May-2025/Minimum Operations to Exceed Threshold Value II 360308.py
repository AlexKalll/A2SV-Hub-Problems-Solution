# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums, k):
        
        heapify (nums)
        ans  = 0
        x = heappop(nums)
        
        while x < k:
            y = heappop(nums)
            nxt = 2*x + y
            x = heappushpop(nums, nxt) # it pops the smallest num x before pushing nxt
            ans+= 1

        return ans