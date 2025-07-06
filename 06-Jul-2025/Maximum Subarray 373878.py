# Problem: Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            curr_max += nums[i]
            if nums[i]  > curr_max:
                curr_max = nums[i]

            ans = max(ans, curr_max)
        
        return ans